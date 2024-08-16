# import Libraries
import enum
from .helper import CONF


class WasteLabel(enum.Enum):
    MW = "0%"
    LW = "0 to 10%"
    MD = "10 to 25%"
    HG = "> 25%"


class ConsumptionLabel(enum.Enum):
    MIC = "Minimal"
    LWC = "Low"
    MDC = "Moderate"
    HGC = "High"


class DietType(enum.Enum):
    VI = "VI"
    VG = "VG"
    FL = "FL"
    PE = "PE"
    OM = "OM"
    CA = "CA"
    KE = "KE"
    PA = "PA"


#  FOOD_FOOTPRINT
FOOD_TYPE_CONVERSION_FACTORS = {
    DietType.VI.value: CONF["VEGAN"],
    DietType.VG.value: CONF["VEGETARIAN"],
    DietType.PE.value: CONF["PESCETARIAN"],
    DietType.FL.value: CONF["FLEXITARIAN"],
    DietType.OM.value: CONF["OMNIVORE"],
    DietType.CA.value: CONF["CARNIVORE"],
    DietType.KE.value: CONF["KETO"],
    DietType.PA.value: CONF["PALEO"],
}


FOOD_CONSUMPTION_CONVERSION_FACTORS = {
    ConsumptionLabel.MIC.value: CONF["MINIMAL_CONSUMPTION"],
    ConsumptionLabel.LWC.value: CONF["LOW_CONSUMPTION"],
    ConsumptionLabel.MDC.value: CONF["MODERATE_CONSUMPTION"],
    ConsumptionLabel.HGC.value: CONF["HIGH_CONSUMPTION"],
    # TODO :Add conversion factors for other units
}


WASTE_LABEL_CONVERSION_FACTORS = {
    WasteLabel.MW.value: CONF["MINIMAL_WASTAGE"],
    WasteLabel.LW.value: CONF["LOW_WASTAGE"],
    WasteLabel.MD.value: CONF["MODERATE_WASTAGE"],
    WasteLabel.HG.value: CONF["HIGH_WASTAGE"],
    # TODO :Add conversion factors for other units
}
