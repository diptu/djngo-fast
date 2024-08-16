import os
import configparser

# Specify the path to your environment file
config_path = os.path.join(os.path.dirname(__file__), "configuration", "config.ini")


def get_config(path=config_path):
    # Load configuration file
    config = configparser.ConfigParser()
    config.read(path)
    conf_vars = {
        # RESIDENTIAL_FOOTPRINT
        "ELECTRICITY_CONSUMPTION_KWH": float(
            config["RESIDENTIAL_FOOTPRINT"]["ELECTRICITY_CONSUMPTION_KWH"]
        ),
        "NATURAL_GAS_CONSUMPTION_KWH": float(
            config["RESIDENTIAL_FOOTPRINT"]["NATURAL_GAS_CONSUMPTION_KWH"]
        ),
        "RENUAL_ENERGY_EMISSION_PER_kWH": float(
            config["RESIDENTIAL_FOOTPRINT"]["RENUAL_ENERGY_EMISSION_PER_kWH"]
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
        "WASTE_RECYCLING_EMISSION_KG": float(
            config["RESIDENTIAL_FOOTPRINT"]["WASTE_RECYCLING_EMISSION_KG"]
        ),
        "WASTE_INCINERATION_EMISSION_KG": float(
            config["RESIDENTIAL_FOOTPRINT"]["WASTE_INCINERATION_EMISSION_KG"]
        ),
    }

    return conf_vars


# Example usage:
CONF = get_config(config_path)
flight_emissions = CONF["ELECTRICITY_CONSUMPTION_KWH"]
print(flight_emissions)
