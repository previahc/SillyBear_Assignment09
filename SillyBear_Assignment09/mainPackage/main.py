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
# Citations:                                                                                                                                                           #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################
import pyodbc
import random
from queryPackage.query import Queries
if __name__ == "__main__":
    
    Queries = Queries()

    products = Queries.get_all_products()

    selected_product = random.choice(products)
    description = selected_product.Description

    product_id = selected_product.ProductID
    manufacturer_id = selected_product.ManufacturerID
    brand_id = selected_product.BrandID

    manufacturer = Queries.get_manufacturer_name(manufacturer_id)

    brand = Queries.get_brand_name(brand_id)
 
   
    number_of_items_sold = Queries.get_number_of_items_sold(product_id)
 
   
    output = f"The product '{description}', manufactured by {manufacturer} and branded as {brand}, has sold {number_of_items_sold} items."
    print(output) 

