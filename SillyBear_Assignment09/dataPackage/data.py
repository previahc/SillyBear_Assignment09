import pyodbc
 
def Data_loader(): 
    """
    Connects to the database and returns the connection object.
    Provides detailed error messages if the connection fails.
    """
    try:
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator ;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )
        return conn
 
    except pyodbc.InterfaceError as e:
        print("Connection failed: Could not connect to the server. Check server name.")
        print("Error details:", e)
    except pyodbc.ProgrammingError as e:
        print("Connection failed: Incorrect database name.")
        print("Error details:", e)
    except pyodbc.Error as e:
        if "28000" in str(e):
            print("Connection failed: Invalid login credentials. Please check the username and password.")
        else:
            print("Connection failed: An unexpected error occurred.")
        print("Error details:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
 
    return None
 
# Attempt to connect