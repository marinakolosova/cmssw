#include "DataFormats/L1TCorrelator/interface/TkElectron.h"
#include "DataFormats/L1TCorrelator/interface/TkElectronFwd.h"
#include "DataFormats/L1TCorrelator/interface/TkEm.h"
#include "DataFormats/L1TCorrelator/interface/TkEmFwd.h"
#include "DataFormats/L1Trigger/interface/EGamma.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/transform.h"

#include "L1Trigger/Phase2L1ParticleFlow/src/newfirmware/dataformats/layer1_emulator.h"
#include <iostream>
#include <vector>

using namespace l1ct;

class L1TCtL2EgProducer : public edm::global::EDProducer<> {
public:
  explicit L1TCtL2EgProducer(const edm::ParameterSet &);
  ~L1TCtL2EgProducer() override;

private:
  void produce(edm::StreamID, edm::Event &,
               const edm::EventSetup &) const override;

  unsigned int mapBoardId(float eta, float phii) const;

  struct RefRemapper {
    typedef TTTrack<Ref_Phase2TrackerDigi_> L1TTTrackType;

    BXVector<edm::Ref<BXVector<l1t::EGamma>>> oldRefs;
    std::map<edm::Ref<BXVector<l1t::EGamma>>, edm::Ref<BXVector<l1t::EGamma>>>
        old2newRefMap;
    std::vector<std::pair<const edm::Ref<l1t::EGammaBxCollection> &,
                          const edm::Ptr<L1TTTrackType> &>>
        origRefAndPtr;
  };

  void convertToEmu(const l1t::TkElectron &tkele, RefRemapper &refRemapper,
                    l1ct::OutputBoard &boarOut) const;
  void convertToEmu(const l1t::TkEm &tkele, RefRemapper &refRemapper,
                    l1ct::OutputBoard &boarOut) const;

  template <class T> class InstanceMerger {
  public:
    InstanceMerger(L1TCtL2EgProducer *prod, const edm::ParameterSet &conf) {
      for (const auto &producer_tag :
           conf.getParameter<std::vector<edm::InputTag>>("pfProducers")) {
        tokens_.push_back(prod->consumes<T>(
            edm::InputTag(producer_tag.label(), producer_tag.instance(),
                          producer_tag.process())));
      }
    }

    const std::vector<edm::EDGetTokenT<T>> &tokens() const { return tokens_; }

  private:
    std::vector<edm::EDGetTokenT<T>> tokens_;
  };

  template <class TT, class T>
  void merge(const InstanceMerger<T> &instance, edm::Event &iEvent,
               RefRemapper &refRemapper, std::unique_ptr<TT> &out) const {
    edm::Handle<T> handle;
    for (const auto &token : instance.tokens()) {
      iEvent.getByToken(token, handle);
      populate(out, handle, refRemapper);
    }
    remapRefs(iEvent, out, refRemapper);
  }

  template <class TT>
  void remapRefs(edm::Event &iEvent, std::unique_ptr<TT> &out,
                 RefRemapper &refRemapper) const {
    // FIXME: remove from design?
    // for (auto& egobj : *out) {
    //   auto newref = refRemapper.old2newRefMap.find(egobj.EGRef());
    //   if (newref != refRemapper.old2newRefMap.end()) {
    //     egobj.setEGRef(newref->second);
    //   }
    // }
  }

  void remapRefs(edm::Event &iEvent,
                 std::unique_ptr<BXVector<l1t::EGamma>> &out,
                 RefRemapper &refRemapper) const {
    edm::RefProd<BXVector<l1t::EGamma>> ref_egs =
        iEvent.getRefBeforePut<BXVector<l1t::EGamma>>(tkEGInstanceLabel_);
    edm::Ref<BXVector<l1t::EGamma>>::key_type idx = 0;
    for (std::size_t ix = 0; ix < out->size(); ix++) {
      refRemapper.old2newRefMap[refRemapper.oldRefs[ix]] =
          edm::Ref<BXVector<l1t::EGamma>>(ref_egs, idx++);
    }
  }

  template <class TT, class T>
  void populate(std::unique_ptr<T> &out, const edm::Handle<TT> &in,
                RefRemapper &refRemapper) const {

    for (unsigned int iBoard = 0, nBoard = in->nRegions(); iBoard < nBoard;
         ++iBoard) {
      auto region = in->region(iBoard);
      float eta = in->eta(iBoard);
      float phi = in->phi(iBoard);
      // FIXME: given eta and phi compute the board index (configurable mapping)
      unsigned int mappedBoardId = mapBoardId(eta, phi);

      for (const auto &obj : region) {
        convertToEmu(obj, refRemapper, out->at(mappedBoardId));
      }
    }
  }

  void populate(std::unique_ptr<BXVector<l1t::EGamma>> &out,
                const edm::Handle<BXVector<l1t::EGamma>> &in,
                RefRemapper &refRemapper) const {
    edm::Ref<BXVector<l1t::EGamma>>::key_type idx = 0;
    for (int bx = in->getFirstBX(); bx <= in->getLastBX(); bx++) {
      for (auto egee_itr = in->begin(bx); egee_itr != in->end(bx); egee_itr++) {
        out->push_back(bx, *egee_itr);
        // this to ensure that the old ref and the new object have the same
        // index in the BXVector collection so that we can still match them no
        // matter which BX we will insert next
        refRemapper.oldRefs.push_back(
            bx, edm::Ref<BXVector<l1t::EGamma>>(in, idx++));
      }
    }
  }

  InstanceMerger<BXVector<l1t::EGamma>> tkEGMerger;
  InstanceMerger<l1t::TkEmRegionalOutput> tkEmMerger;
  InstanceMerger<l1t::TkElectronRegionalOutput> tkEleMerger;
  std::string tkEGInstanceLabel_;
  std::map<std::pair<double, double>, unsigned int> board_map_;

};

L1TCtL2EgProducer::L1TCtL2EgProducer(const edm::ParameterSet &conf)
    : tkEGMerger(this, conf.getParameter<edm::ParameterSet>("tkEgs")),
      tkEmMerger(this, conf.getParameter<edm::ParameterSet>("tkEms")),
      tkEleMerger(this, conf.getParameter<edm::ParameterSet>("tkElectrons")),
      tkEGInstanceLabel_(conf.getParameter<std::string>("tkEGInstanceLabel")) {

  produces<BXVector<l1t::EGamma>>(tkEGInstanceLabel_);
  
  for(const auto& pset: conf.getParameter<std::vector<edm::ParameterSet>>("boards")) {
    board_map_[std::make_pair(pset.getParameter<double>("eta"), pset.getParameter<double>("phi"))] = pset.getParameter<uint32_t>("index");
  }
}

L1TCtL2EgProducer::~L1TCtL2EgProducer() {}

void L1TCtL2EgProducer::produce(edm::StreamID, edm::Event &iEvent,
                                const edm::EventSetup &) const {
  RefRemapper refmapper;

  auto outEgs = std::make_unique<BXVector<l1t::EGamma>>();
  merge(tkEGMerger, iEvent, refmapper, outEgs);
  iEvent.put(std::move(outEgs), tkEGInstanceLabel_);

  auto boards = std::make_unique<std::vector<l1ct::OutputBoard>>(board_map_.size());

  merge(tkEleMerger, iEvent, refmapper, boards);
  merge(tkEmMerger, iEvent, refmapper, boards);
  //
  //
  // l2sorterEmulator-> run(const std::vector<l1ct::OutputBoard> &in,
  //              std::vector<EGIsoObjEmu> &out_photons,
  //              std::vector<EGIsoEleObjEmu> &out_eles) const;
}

unsigned int L1TCtL2EgProducer::mapBoardId(float eta, float phi) const {
  const auto idxitr = board_map_.find(std::make_pair(eta, phi));
  // FIXME: is it ok?
  // throw cms::Exception("Configuration", "caloSectors phi range too large for phi_t data type");

  assert(idxitr != board_map_.end());
  return idxitr->second;
}

void L1TCtL2EgProducer::convertToEmu(const l1t::TkElectron &tkele,
                                     RefRemapper &refRemapper,
                                     l1ct::OutputBoard &boarOut) const {
  EGIsoEleObjEmu emu;
  emu.initFromBits(tkele.egBinaryWord<EGIsoEleObj::BITWIDTH>());
  emu.srcCluster = nullptr;
  emu.srcTrack = nullptr;
  auto refEg = tkele.EGRef();
  const auto newref = refRemapper.old2newRefMap.find(refEg);
  if (newref != refRemapper.old2newRefMap.end()) {
    refEg = newref->second;
  }
  refRemapper.origRefAndPtr.push_back(std::make_pair(refEg, tkele.trkPtr()));
  emu.sta_idx = refRemapper.origRefAndPtr.size() - 1;
  emu.setHwIso(EGIsoEleObjEmu::IsoType::TkIso,
               l1ct::Scales::makeIso(tkele.trkIsol()));
  emu.setHwIso(EGIsoEleObjEmu::IsoType::PfIso,
               l1ct::Scales::makeIso(tkele.pfIsol()));
  boarOut.egelectron.push_back(emu);
}

void L1TCtL2EgProducer::convertToEmu(const l1t::TkEm &tkem,
                                     RefRemapper &refRemapper,
                                     l1ct::OutputBoard &boarOut) const {
  EGIsoObjEmu emu;
  emu.initFromBits(tkem.egBinaryWord<EGIsoObj::BITWIDTH>());
  emu.srcCluster = nullptr;
  auto refEg = tkem.EGRef();
  const auto newref = refRemapper.old2newRefMap.find(refEg);
  if (newref != refRemapper.old2newRefMap.end()) {
    refEg = newref->second;
  }
  refRemapper.origRefAndPtr.push_back(
      std::make_pair(refEg, edm::Ptr<RefRemapper::L1TTTrackType>(nullptr, 0)));
  emu.sta_idx = refRemapper.origRefAndPtr.size() - 1;
  emu.setHwIso(EGIsoObjEmu::IsoType::TkIso,
               l1ct::Scales::makeIso(tkem.trkIsol()));
  emu.setHwIso(EGIsoObjEmu::IsoType::PfIso,
               l1ct::Scales::makeIso(tkem.pfIsol()));
  emu.setHwIso(EGIsoObjEmu::IsoType::TkIsoPV,
               l1ct::Scales::makeIso(tkem.trkIsolPV()));
  emu.setHwIso(EGIsoObjEmu::IsoType::PfIsoPV,
               l1ct::Scales::makeIso(tkem.pfIsolPV()));

  boarOut.egphoton.push_back(emu);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(L1TCtL2EgProducer);
