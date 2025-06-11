import oracledb

def get_connection():
    connection = oracledb.connect(
        user="bank_admin",
        password="root",  # or whatever password you set
        dsn="localhost/XEPDB1"
    )
    return connection
