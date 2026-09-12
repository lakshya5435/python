import oracledb
db_user = "system"
db_password = "Laksh435"

db_dsn = "localhost:1521/FREEPDB1"

print("Attempting to connect to Oracle...")

try:
   
    connection = oracledb.connect(
        user=db_user,
        password=db_password,
        dsn=db_dsn
    )
    print("✅ Successfully connected to the database!\n")
    
   
    with connection.cursor() as cursor:
       
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
   
    if 'connection' in locals():
        connection.close()