import os
import configparser

# Specify the path to your environment file
config_path = os.path.join(os.path.dirname(__file__), "configuration", "config.ini")


def get_config(path=config_path):
    # Load configuration file
    config = configparser.ConfigParser()
    config.read(path)
    conf_vars = {
        # DIET_TYPE
        "VEGAN": float(config["DIET_TYPE"]["VEGAN"]),
        "VEGETARIAN": float(config["DIET_TYPE"]["VEGETARIAN"]),
        "PESCETARIAN": float(config["DIET_TYPE"]["PESCETARIAN"]),
        "FLEXITARIAN": float(config["DIET_TYPE"]["FLEXITARIAN"]),
        "OMNIVORE": float(config["DIET_TYPE"]["OMNIVORE"]),
        "CARNIVORE": float(config["DIET_TYPE"]["CARNIVORE"]),
        "KETO": float(config["DIET_TYPE"]["KETO"]),
        "PALEO": float(config["DIET_TYPE"]["PALEO"]),
        # CONSUMPTION LABEL
        "MINIMAL_CONSUMPTION": float(config["LEVEL_OF_CONSUMPTION"]["MINIMAL"]),
        "LOW_CONSUMPTION": float(config["LEVEL_OF_CONSUMPTION"]["LOW"]),
        "MODERATE_CONSUMPTION": float(config["LEVEL_OF_CONSUMPTION"]["MODERATE"]),
        "HIGH_CONSUMPTION": float(config["LEVEL_OF_CONSUMPTION"]["HIGH"]),
        # WASTAGE LABEL
        "MINIMAL_WASTAGE": float(config["LEVEL_OF_WASTAGE"]["MINIMAL"]),
        "LOW_WASTAGE": float(config["LEVEL_OF_WASTAGE"]["LOW"]),
        "MODERATE_WASTAGE": float(config["LEVEL_OF_WASTAGE"]["MODERATE"]),
        "HIGH_WASTAGE": float(config["LEVEL_OF_WASTAGE"]["HIGH"]),
    }

    return conf_vars


# Example usage:
CONF = get_config(config_path)
flight_emissions = CONF["LOW_CONSUMPTION"]
print(flight_emissions)
