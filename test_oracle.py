import oracledb

# Database credentials
db_user = "system"
db_password = "Laksh435"

# Connection string: hostname:port/service_name
db_dsn = "localhost:1521/FREEPDB1"

print("Attempting to connect to Oracle...")

try:
    # Establish the connection
    connection = oracledb.connect(
        user=db_user,
        password=db_password,
        dsn=db_dsn
    )
    print("✅ Successfully connected to the database!\n")
    
    # Open a cursor to execute a query
    with connection.cursor() as cursor:
        # Query the database version
        cursor.execute("SELECT banner FROM v$version")
        version = cursor.fetchone()
        
        print("Database Version Info:")
        print("-" * 20)
        print(version[0])
        
except oracledb.DatabaseError as e:
    error, = e.args
    print("❌ Connection failed!")
    print(f"Error Code: {error.code}")
    print(f"Error Message: {error.message}")
    
finally:
    # Always close the connection when done
    if 'connection' in locals():
        connection.close()