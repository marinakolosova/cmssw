#ifndef FEDRawData_FEDRawDataCollection_h
#define FEDRawData_FEDRawDataCollection_h

/** \class FEDRawDataCollection
 *  An EDCollection storing the raw data for all  FEDs in a Event.
 *  
 *  Reference: DaqPrototype/DaqPersistentData/interface/DaqFEDOpaqueData.h
 *
 *  \author N. Amapane - S. Argiro'
 */

#include <DataFormats/FEDRawData/interface/FEDRawData.h>
#include "DataFormats/Common/interface/traits.h"
#include "FWCore/Utilities/interface/GCCPrerequisite.h"

#include <vector>

class FEDRawDataCollection : public edm::DoNotRecordParents {
public:
  FEDRawDataCollection();

  virtual ~FEDRawDataCollection();

  /// retrieve data for fed @param fedid
  const FEDRawData& FEDData(int fedid) const;

  /// retrieve data for fed @param fedid
  FEDRawData& FEDData(int fedid);

  FEDRawDataCollection(const FEDRawDataCollection&);

  FEDRawDataCollection& operator=(const FEDRawDataCollection&) = default;

  void swap(FEDRawDataCollection& other) { data_.swap(other.data_); }

private:
  std::vector<FEDRawData> data_;  ///< the raw data
};

inline void swap(FEDRawDataCollection& a, FEDRawDataCollection& b) { a.swap(b); }

#endif
