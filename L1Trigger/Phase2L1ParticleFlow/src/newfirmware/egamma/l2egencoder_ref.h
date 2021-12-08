#ifndef L2EGENCODER_REF_H
#define L2EGENCODER_REF_H

#ifdef CMSSW_GIT_HASH
#include "../dataformats/layer1_emulator.h"
#include "../dataformats/egamma.h"
#include "L1Trigger/Phase2L1ParticleFlow/src/dbgPrintf.h"

#else
#include "../../dataformats/layer1_emulator.h"
#include "../../dataformats/egamma.h"
#include "../../utils/dbgPrintf.h"

#endif

namespace edm {
  class ParameterSet;
}

namespace l1ct {

  struct L2EgEncoderEmulator {
  public:
    L2EgEncoderEmulator(unsigned int nEncodedWords) : nEncodedWords_(nEncodedWords){};

    L2EgEncoderEmulator(const edm::ParameterSet& iConfig);

    void toFirmware(const std::vector<ap_uint<64>>& encoded_in, ap_uint<64> encoded_fw[]) const;

    std::vector<ap_uint<64>> encodeLayer2EgObjs(unsigned int nObj,
                                                const std::vector<EGIsoObjEmu>& photons,
                                                const std::vector<EGIsoEleObjEmu>& electrons) const {
      std::vector<ap_uint<64>> ret;

      auto encoded_photons = encodeLayer2(photons);
      encoded_photons.resize(nObj, {0});
      auto encoded_eles = encodeLayer2(electrons);
      encoded_eles.resize(nObj, {0});
      //
      encodeLayer2To64bits(encoded_photons, ret);
      encodeLayer2To64bits(encoded_eles, ret);

      return ret;
    }

  private:
    template <class T>
    ap_uint<96> encodeLayer2(const T& egiso) const {
      ap_uint<96> ret = 0;
      // FIXME; should be packed in GT format
      ret(T::BITWIDTH - 1, 0) = egiso.pack();
      return ret;
    }

    template <class T>
    std::vector<ap_uint<96>> encodeLayer2(const std::vector<T>& egisos) const {
      std::vector<ap_uint<96>> ret;
      for (const auto& egiso : egisos) {
        ret.push_back(encodeLayer2(egiso));
      }
      return ret;
    }
    //

    void encodeLayer2To64bits(const std::vector<ap_uint<96>>& packed96, std::vector<ap_uint<64>>& packed64) const {
      for (unsigned int i = 0; i < packed96.size(); i += 2) {
        packed64.push_back(packed96[i](63, 0));
        packed64.push_back((ap_uint<32>(packed96[i + 1](95, 64)), ap_uint<32>(packed96[i](95, 64))));
        packed64.push_back(packed96[i + 1](63, 0));

        // std::cout << "obj [" << i << "]: " << std::hex << packed96[i] << std::endl;
        // std::cout << "obj [" << i+1 << "]: " << std::hex << packed96[i+1] << std::endl;
        // std::cout << "frame [" << std::dec << packed64.size()-3 << "]" << std::hex << packed64[packed64.size()-3] << std::endl;
        // std::cout << "frame [" << std::dec << packed64.size()-2 << "]" << std::hex << packed64[packed64.size()-2] << std::endl;
        // std::cout << "frame [" << std::dec << packed64.size()-1 << "]" << std::hex << packed64[packed64.size()-1] << std::endl;
      }
    }

    unsigned int nEncodedWords_;
  };

}  // namespace l1ct
#endif
