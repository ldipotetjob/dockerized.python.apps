import psycopg2
import os

## db_hostname = os.getenv("DBENDP", default=None)
## db_username = os.getenv("DBUSER", default=None)
## passwd = os.getenv("DBPASS", default=None)
## port = os.getenv("DBPORT", default=None)

db_hostname = "localhost"
db_username = "postgres"
passwd = "postgres"
port = 5432

try:
    conn = psycopg2.connect(
        host=db_hostname, user=db_username, password=passwd, port=port, dbname="genhub"
    )
    cursor = conn.cursor()
    cursor.execute("select * from genhubrequest;")
    for record in cursor:
        print(record)
    conn.close()
except Exception as e:
    print("Exception: ", e)