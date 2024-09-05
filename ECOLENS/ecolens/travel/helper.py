import os
import configparser

# Specify the path to your environment file
config_path = os.path.join(os.path.dirname(__file__), "configuration", "config.ini")


def get_config(path=config_path):
    # Load configuration file
    config = configparser.ConfigParser()
    config.read(path)
    conf_vars = {
        # BUSINESS_TRAVEL
        "BUSINESS_FLIGHT_EMISSIONS_PER_KM": float(
            config["BUSINESS_TRAVEL"]["FLIGHT_EMISSIONS_PER_KM"]
        ),
        "BUSINESS_TRANSIT_EMISSIONS_PER_KM": float(
            config["BUSINESS_TRAVEL"]["TRANSIT_EMISSIONS_PER_KM"]
        ),
        # CAR_EMISSION_COMPANY_VEHICLES
        "BUSINESS_GASOLINE_CAR_MANUFACTURING_EMISSIONS": float(
            config["CAR_EMISSION_COMPANY_VEHICLES"][
                "GASOLINE_CAR_MANUFACTURING_EMISSIONS"
            ]
        ),
        "BUSINESS_DIESEL_CAR_MANUFACTURING_EMISSIONS": float(
            config["CAR_EMISSION_COMPANY_VEHICLES"][
                "DIESEL_CAR_MANUFACTURING_EMISSIONS"
            ]
        ),
        "BUSINESS_ELECTRIC_CAR_MANUFACTURING_EMISSIONS": float(
            config["CAR_EMISSION_COMPANY_VEHICLES"][
                "ELECTRIC_CAR_MANUFACTURING_EMISSIONS"
            ]
        ),
        "BUSINESS_HYBRID_CAR_MANUFACTURING_EMISSIONS": float(
            config["CAR_EMISSION_COMPANY_VEHICLES"][
                "HYBRID_CAR_MANUFACTURING_EMISSIONS"
            ]
        ),
        "BUSINESS_GASOLINE_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION_COMPANY_VEHICLES"]["GASOLINE_CAR_EMISSIONS_PER_KM"]
        ),
        "BUSINESS_DISEL_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION_COMPANY_VEHICLES"]["DISEL_CAR_EMISSIONS_PER_KM"]
        ),
        "BUSINESS_ELECTRIC_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION_COMPANY_VEHICLES"]["ELECTRIC_CAR_EMISSIONS_PER_KM"]
        ),
        "BUSINESS_HYBRID_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION_COMPANY_VEHICLES"]["HYBRID_CAR_EMISSIONS_PER_KM"]
        ),
        # CAR_EMISSION_STAFF_COMMUTE
        "STAFF_GASOLINE_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION_STAFF_COMMUTE"]["GASOLINE_CAR_EMISSIONS_PER_KM"]
        ),
        "STAFF_DISEL_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION_STAFF_COMMUTE"]["DISEL_CAR_EMISSIONS_PER_KM"]
        ),
        "STAFF_ELECTRIC_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION_STAFF_COMMUTE"]["ELECTRIC_CAR_EMISSIONS_PER_KM"]
        ),
        "STAFF_HYBRID_CAR_EMISSIONS_PER_KM": float(
            config["CAR_EMISSION_STAFF_COMMUTE"]["HYBRID_CAR_EMISSIONS_PER_KM"]
        ),
    }

    return conf_vars


# Example usage:
CONF = get_config(config_path)
flight_emissions = CONF["BUSINESS_FLIGHT_EMISSIONS_PER_KM"]
print(flight_emissions)
