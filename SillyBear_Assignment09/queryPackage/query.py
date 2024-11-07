########################################################################################################################################################################
# Name: Will Padgett, Aryan Patel, Heitor Previatti                                                                                                                    #
# email:  padgetwg@mail.uc.edu, patel7ag@mail.uc.edu, peviahc@mail.uc.edu                                                                                              #
# Assignment Number: Assignment 09                                                                                                                                     #
# Due Date:   11/07/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment:collaborate with peers to develop a VS project that querys data from a database                                                  #                                                                                                                                                                  
# Brief Description of what this module does.  This module demonstrates funtionality of product and supplier.py                                                        #                                       
#                                                                                                                                                                      #
# Citations: W3 Schools                                                                                                                                                #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################
import pyodbc
from dataPackage.data import Data_loader
import random


class Queries:
    def __init__(self):
            self.conn = Data_loader()
            self.cursor = self.conn.cursor()

    def get_all_products(self):
        """Fetch all products."""
        product_query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
        self.cursor.execute(product_query)
        return self.cursor.fetchall()

    def get_manufacturer_name(self, manufacturer_id):
        """Get manufacturer name."""
        manufacturer_query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
        self.cursor.execute(manufacturer_query)
        result = self.cursor.fetchone()
        return result[0] if result else "Unknown Manufacturer"

    def get_brand_name(self, brand_id):
        """Get brand name."""
        brand_query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
        self.cursor.execute(brand_query)
        result = self.cursor.fetchone()
        return result[0] if result else "Unknown Brand"

    def get_number_of_items_sold(self, product_id):
        """Get number of items sold."""
        sales_query = f"""
        SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
        FROM dbo.tTransactionDetail 
        INNER JOIN dbo.tTransaction 
        ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID 
        WHERE dbo.tTransaction.TransactionTypeID = 1 
        AND dbo.tTransactionDetail.ProductID = {product_id}
        """
        self.cursor.execute(sales_query)
        result = self.cursor.fetchone()
        return result[0] if result and result[0] is not None else 0

    def close_connection(self):
        """Close connection."""
        self.cursor.close()
        self.conn.close()

