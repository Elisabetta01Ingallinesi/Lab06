from database.Sales_DAO import Sales_DAO
from database.Product_DAO import Product_DAO
from database.Retailer_DAO import Retailer_DAO
class Model:
    def __init__(self):
        pass

    def get_anno(self):
        return Sales_DAO.get_anno()

    def get_brand(self):
        return Product_DAO.get_brand()

    def get_retailer(self):
        return Retailer_DAO.get_retailer()

    def get_top_vendite(self, anno, brand, reteiler):
        return Sales_DAO.get_top_vendite(anno, brand, reteiler)