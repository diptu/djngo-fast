# import Libraries
import enum
from .helper import CONF


class EnergyUnit(enum.Enum):
    KWh = "KWh"
    Wh = "Wh"


class DistanceUnit(enum.Enum):
    Km = "Km"
    Mi = "Mi"


class AreaUnit(enum.Enum):
    m2 = "m2"
    # km2 = "km2"


class VolumeUnit(enum.Enum):
    L = "L"
    KL = "KL"


class MassUnit(enum.Enum):
    Kg = "Kg"
    Lb = "Lb"


#  RESIDENTIAL_FOOTPRINT
ELECTRICITY_EMISSION_CONVERSION_FACTORS = {
    EnergyUnit.KWh.value: CONF["ELECTRICITY_CONSUMPTION_KWH"],
    EnergyUnit.Wh.value: 0.000000481,  # TODO : MODiFY With correct value
    # Add conversion factors for other units
}
NATURAL_GAS_EMISSIONS_CONVERSION_FACTORS = {
    EnergyUnit.KWh.value: CONF["NATURAL_GAS_CONSUMPTION_KWH"],
}

RENUAL_ENERGY_EMISSION_CONVERSION_FACTORS = {
    EnergyUnit.KWh.value: CONF["RENUAL_ENERGY_EMISSION_PER_kWH"],
}

HEATING_OIL_USAGES_EMISSIONS_CONVERSION_FACTORS = {
    VolumeUnit.L.value: CONF["HEATING_OIL_CONSUMPTION_LITRE"],
}

WATER_USAGES_EMISSIONS_CONVERSION_FACTORS = {
    VolumeUnit.L.value: CONF["WATER_USAGES_LITRE"],
}
LIVING_SPACE_CONSTRUCTION_EMISSION_CONVERSION_FACTORS = {
    AreaUnit.m2.value: CONF["LIVING_SPACE_CONSTRUCTION_EMISSION_M2"],
}

WASTE_RECYCLING_EMISSIONS_CONVERSION_FACTORS = {
    MassUnit.Kg.value: CONF["WASTE_RECYCLING_EMISSION_KG"],
}
WASTE_INCINERATION_EMISSIONS_CONVERSION_FACTORS = {
    MassUnit.Kg.value: CONF["WASTE_INCINERATION_EMISSION_KG"],
}
