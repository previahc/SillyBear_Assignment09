
import pyodbc
import random
from queryPackage.query import Queries
if __name__ == "__main__":
    # Initialize the ProductAnalytics class
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

