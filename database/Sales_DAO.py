from model.Sales import Sales
from database.DB_connect import DBConnect
class Sales_DAO:

    @staticmethod
    def get_anno():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Nessuna connessione")
            return None
        cursor = cnx.cursor()
        query = """select distinct year(date)
                    from go_daily_sales """
        cursor.execute(query)
        for row in cursor:
            result.append(row[0])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_top_vendite(anno, brand, reteiler):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Nessuna connessione")
            return None
        cursor = cnx.cursor(dictionary = True)
        query = """ select *
                    from go_daily_sales gds, go_products gp  
                    where gds.Product_number = gp.Product_number and 
	                year(date) = coalesce (%s, year(date)) and 
	                gp.Product_brand = coalesce (%s, gp.Product_brand) and 
	                gds.Retailer_code = coalesce (%s, gds.Retailer_code) """
        cursor.execute(query, [anno, brand, reteiler])
        for row in cursor:
            result.append(Sales(row["Retailer_code"], row["Product_number"], row["Order_method_code"],
                                row["Date"], row["Quantity"], row["Unit_price"], row["Unit_sale_price"],
                                row["Quantity"]*row["Unit_sale_price"]))
        cursor.close()
        cnx.close()
        return result




