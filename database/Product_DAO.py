from database.DB_connect import DBConnect
from model.Product import Product

class Product_DAO:

    @staticmethod
    def get_brand():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Nessuna connessione")
            return None
        cursor = cnx.cursor()
        query = """select distinct Product_brand 
                    from go_products  """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result