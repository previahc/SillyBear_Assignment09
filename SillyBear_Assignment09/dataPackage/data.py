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
class Loader:
    
    def Data_loader(): 
        """
        Connects to the database and returns the connection object.
        Provides detailed error messages if the connection fails.
        """
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator ;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )
        return conn
 
   
