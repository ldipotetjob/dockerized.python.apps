import psycopg2
import os
import time

from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)


def get_genhubrequest():
    ## db_hostname = os.getenv("DBENDP", default=None)
    ## db_username = os.getenv("DBUSER", default=None)
    ## passwd = os.getenv("DBPASS", default=None)
    ## port = os.getenv("DBPORT", default=None)
    db_hostname = os.getenv("POSTGRES_IPADDRESS")
    db_username = "genhub"
    passwd = "genhub"
    port = 5432

    ##try:
    conn = psycopg2.connect(host=db_hostname, user=db_username, password=passwd, port=port, dbname="genhub")
    cursor = conn.cursor()
    cursor.execute("select * from genhubrequest;")
        ##        for record in cursor:
        ##        print(record)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    ##except Exception as e:
    ##    print("Exception: ", e)
    return render_template('index.html', data=data)

@app.route('/')
def index():
    ##   return 'Hello , we are in genhub request'
    return get_genhubrequest()
