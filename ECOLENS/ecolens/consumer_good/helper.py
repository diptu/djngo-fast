import os
import configparser

# Specify the path to your environment file
config_path = os.path.join(os.path.dirname(__file__), "configuration", "config.ini")


def get_config(path=config_path):
    # Load configuration file
    config = configparser.ConfigParser()
    config.read(path)
    conf_vars = {
        # CONSUMER_GOODS_AND_SERVICES
        "CLOTHING": float(config["CLOTHING"]["AMOUNT_SPENT_FACTORS"]),
        "APPLIANCES": float(config["APPLIANCES"]["AMOUNT_SPENT_FACTORS"]),
        "PHARMACEUTICALS": float(config["PHARMACEUTICALS"]["AMOUNT_SPENT_FACTORS"]),
        "FURNITURE": float(config["FURNITURE"]["AMOUNT_SPENT_FACTORS"]),
        "HOSPITALITY": float(config["HOSPITALITY"]["AMOUNT_SPENT_FACTORS"]),
        "SERVICES": float(config["SERVICES"]["AMOUNT_SPENT_FACTORS"]),
    }

    return conf_vars


# Example usage:
CONF = get_config(config_path)
flight_emissions = CONF["HOSPITALITY"]
print(flight_emissions)
