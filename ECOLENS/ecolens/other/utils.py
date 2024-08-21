# import Libraries
# import enum
from ecolens.enums import Others
from .helper import CONF


# class Others(enum.Enum):
#     E = "EDUCATION"
#     A = "ACTIVITIES"
#     P = "PUBLIC_SERVICES"


#  OTHER_FOOTPRINT
OTHERS_CONVERSION_FACTORS = {
    Others.E.value: CONF["EDUCATION"],
    Others.A.value: CONF["ACTIVITIES"],
    Others.P.value: CONF["PUBLIC_SERVICES"],
}
