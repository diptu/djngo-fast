import os
import configparser

# Specify the path to your environment file
config_path = os.path.join(os.path.dirname(__file__), "configuration", "config.ini")


def get_config(path=config_path):
    # Load configuration file
    config = configparser.ConfigParser()
    config.read(path)
    conf_vars = {
        # FLIGHT_EMISSIONS_PER_KM
        "FLIGHT_EMISSIONS_PER_KM": float(
            config["VEHICLE_EMISSION_METRICS"]["FLIGHT_EMISSIONS_PER_KM"]
        ),
        "TRANSIT_EMISSIONS_PER_KM": float(
            config["VEHICLE_EMISSION_METRICS"]["TRANSIT_EMISSIONS_PER_KM"]
        ),
        # VEHICLE_MANUFACTURING_EMISSION
        "GASOLINE_CAR_MANUFACTURING_EMISSIONS": float(
            config["VEHICLE_MANUFACTURING_EMISSION"][
                "GASOLINE_CAR_MANUFACTURING_EMISSIONS"
            ]
        ),
        "DIESEL_CAR_MANUFACTURING_EMISSIONS": float(
            config["VEHICLE_MANUFACTURING_EMISSION"][
                "DIESEL_CAR_MANUFACTURING_EMISSIONS"
            ]
        ),
        "ELECTRIC_CAR_MANUFACTURING_EMISSIONS": float(
            config["VEHICLE_MANUFACTURING_EMISSION"][
                "ELECTRIC_CAR_MANUFACTURING_EMISSIONS"
            ]
        ),
        "HYBRID_CAR_MANUFACTURING_EMISSIONS": float(
            config["VEHICLE_MANUFACTURING_EMISSION"][
                "HYBRID_CAR_MANUFACTURING_EMISSIONS"
            ]
        ),
        # CAR_EMISSION
        "GASOLINE_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION"]["GASOLINE_CAR_EMISSIONS_PER_KM"]
        ),
        "DISEL_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION"]["DISEL_CAR_EMISSIONS_PER_KM"]
        ),
        "ELECTRIC_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION"]["ELECTRIC_CAR_EMISSIONS_PER_KM"]
        ),
        "HYBRID_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION"]["HYBRID_CAR_EMISSIONS_PER_KM"]
        ),
        # RESIDENTIAL_FOOTPRINT
        "ELECTRICITY_CONSUMPTION_KWH": float(
            config["RESIDENTIAL_FOOTPRINT"]["ELECTRICITY_CONSUMPTION_KWH"]
        ),
        "NATURAL_GAS_CONSUMPTION_KWH": float(
            config["RESIDENTIAL_FOOTPRINT"]["NATURAL_GAS_CONSUMPTION_KWH"]
        ),
        "HEATING_OIL_CONSUMPTION_LITRE": float(
            config["RESIDENTIAL_FOOTPRINT"]["HEATING_OIL_CONSUMPTION_LITRE"]
        ),
        "WATER_USAGES_LITRE": float(
            config["RESIDENTIAL_FOOTPRINT"]["WATER_USAGES_LITRE"]
        ),
        "LIVING_SPACE_CONSTRUCTION_EMISSION_M2": float(
            config["RESIDENTIAL_FOOTPRINT"]["LIVING_SPACE_CONSTRUCTION_EMISSION_M2"]
        ),
    }

    return conf_vars


# Example usage:
CONF = get_config(config_path)
# flight_emissions = CONF["FLIGHT_EMISSIONS_PER_KM"]
# print(flight_emissions)
