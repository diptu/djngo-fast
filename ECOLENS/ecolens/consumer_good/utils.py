# import Libraries
import enum
from .helper import CONF


# class GOODSANDSERVICES(enum.Enum):
#     ECU = "tCO2equ/USD"


class GoodsAndServices(enum.Enum):
    C = "CLOTHING"
    A = "APPLIANCES"
    P = "PHARMACEUTICALS"
    F = "FURNITURE"
    H = "HOSPITALITY"
    S = "SERVICES"


#  FOOD_FOOTPRINT
CONSUMER_GOODS_AND_SERVICES_CONVERSION_FACTORS = {
    GoodsAndServices.C.value: CONF["CLOTHING"],
    GoodsAndServices.A.value: CONF["APPLIANCES"],
    GoodsAndServices.P.value: CONF["PHARMACEUTICALS"],
    GoodsAndServices.F.value: CONF["FURNITURE"],
    GoodsAndServices.H.value: CONF["HOSPITALITY"],
    GoodsAndServices.S.value: CONF["SERVICES"],
}
