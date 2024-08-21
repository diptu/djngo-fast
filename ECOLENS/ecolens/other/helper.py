import os
import configparser

# Specify the path to your environment file
config_path = os.path.join(os.path.dirname(__file__), "configuration", "config.ini")


def get_config(path=config_path):
    # Load configuration file
    config = configparser.ConfigParser()
    config.read(path)
    conf_vars = {
        # MISCELLANEOUS
        "EDUCATION": float(config["EDUCATION"]["AMOUNT_SPENT_FACTORS"]),
        "ACTIVITIES": float(config["ACTIVITIES"]["AMOUNT_SPENT_FACTORS"]),
        "PUBLIC_SERVICES": float(config["PUBLIC_SERVICES"]["AMOUNT_SPENT_FACTORS"]),
    }

    return conf_vars


# Example usage:
CONF = get_config(config_path)
flight_emissions = CONF["ACTIVITIES"]
print(flight_emissions)
