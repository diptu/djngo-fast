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


# class CarType(enum.Enum):
#     E = "Electric"
#     G = "Gasoline"
#     D = "Diesel"
#     H = "Hybrid"


# print(f"DistanceUnit.Km:{DistanceUnit.Km.value}")
# VEHICLE_EMISSION_METRICS
FLIGHT_DISTANCE_CONVERSION_FACTORS = {
    DistanceUnit.Km.value: CONF["FLIGHT_EMISSIONS_PER_KM"],
    DistanceUnit.Mi.value: 1.60934,  # TODO : MODiFY With correct value
    # Add conversion factors for other units
}

PUBLIC_TRNSIT_CONVERSION_FACTORS = {
    DistanceUnit.Km.value: CONF["TRANSIT_EMISSIONS_PER_KM"],
}
# Vehicle Manufacturing Emissions
GASOLINE_CAR_MANUFACTURING_EMISSIONS = {
    DistanceUnit.Km.value: CONF["GASOLINE_CAR_MANUFACTURING_EMISSIONS"],
}

DIESEL_CAR_MANUFACTURING_EMISSIONS = {
    DistanceUnit.Km.value: CONF["DIESEL_CAR_MANUFACTURING_EMISSIONS"],
}

ELECTRIC_CAR_MANUFACTURING_EMISSIONS = {
    DistanceUnit.Km.value: CONF["ELECTRIC_CAR_MANUFACTURING_EMISSIONS"],
}

HYBRID_CAR_MANUFACTURING_EMISSIONS = {
    DistanceUnit.Km.value: CONF["HYBRID_CAR_MANUFACTURING_EMISSIONS"],
}


# Car Emissions
GASOLINE_CAR_EMISSIONS_PER_KM = {
    DistanceUnit.Km.value: CONF["GASOLINE_CAR_EMISSIONS_PER_KM"],
}

DISEL_CAR_EMISSIONS_PER_KM = {
    DistanceUnit.Km.value: CONF["DISEL_CAR_EMISSIONS_PER_KM"],
}

ELECTRIC_CAR_EMISSIONS_PER_KM = {
    DistanceUnit.Km.value: CONF["ELECTRIC_CAR_EMISSIONS_PER_KM"],
}
HYBRID_CAR_EMISSIONS_PER_KM = {
    DistanceUnit.Km.value: CONF["HYBRID_CAR_EMISSIONS_PER_KM"],
}


# Residential Footprint
ELECTRICITY_CONSUMPTION_KWH = {
    DistanceUnit.Km.value: CONF["ELECTRICITY_CONSUMPTION_KWH"],
}


NATURAL_GAS_CONSUMPTION_KWH = {
    EnergyUnit.KWh.value: CONF["NATURAL_GAS_CONSUMPTION_KWH"],
}

HEATING_OIL_CONSUMPTION_LITRE = {
    VolumeUnit.L.value: CONF["HEATING_OIL_CONSUMPTION_LITRE"],
}

WATER_USAGES_LITRE = {
    VolumeUnit.L.value: CONF["WATER_USAGES_LITRE"],
}
LIVING_SPACE_CONSTRUCTION_EMISSION_M2 = {
    AreaUnit.m2.value: CONF["LIVING_SPACE_CONSTRUCTION_EMISSION_M2"],
}
