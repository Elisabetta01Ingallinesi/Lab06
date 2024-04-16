from database.DB_connect import DBConnect
from model.Retailer import Retailer

class Retailer_DAO:
    @staticmethod
    def get_retailer():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Nessuna connessione")
            return None
        cursor = cnx.cursor(dictionary= True)
        query = """ select *
                    from go_retailers """
        cursor.execute(query)
        for row in cursor:
            result.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))
        cursor.close()
        cnx.close()
        return result