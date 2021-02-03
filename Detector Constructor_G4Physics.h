#ifndef Detector Construction_h
#define DetectorConstruction_h 1

#include "G4VUserDetectorConstruction.hh"
#include "globals.hh"
#include "G4Material.hh"
#include "G4ProductionCuts.hh"

class G4PhysicalVolume;
class G4LogicalVolume;

class DetectorConstruction : public G4UserDetectionConstruction
{
	public:
	//constructor ad Destructor
	DetectorConstruction();
	virtual -DetectorConstruction();
	|
	//member Function
	void DefineMaterial();
	G4PhysicalVolume* Construct();
	void ConstructSDandField();
	G4LogicalVolume* detectorLog;
	private:
	G4bool             fChecOverlaps;
	G4Material*         fEmptyMat;
	G4Material*         fDetMat;
	G4ProductionCuts*   fDetectorCuts;
};
#endif

	