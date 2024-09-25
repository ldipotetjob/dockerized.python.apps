import psycopg2
import os
import time

from flask import Flask, render_template, request, redirect, url_for
import psycopg2

# ref.: solution avoiding the comment:
# genhub-app  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# @ see: https://stackoverflow.com/a/54381386/3848652

app = Flask(__name__)

# db_hostname = os.getenv("DBENDP", default=None)
# db_username = os.getenv("DBUSER", default=None)
# passwd = os.getenv("DBPASS", default=None)
# port = os.getenv("DBPORT", default=None)

db_hostname = os.getenv("POSTGRES_IPADDRESS")
db_username = "genhub"
passwd = "genhub"
port = 5432

conn = psycopg2.connect(host=db_hostname, user=db_username, password=passwd, port=port, dbname="genhub")
global data_get


def get_genhubrequest():
    global data_get

    try:
        cursor = conn.cursor()
        cursor.execute("select * from genhubrequest;")
        # for record in cursor:
        #   print(record)
        data_get = cursor.fetchall()
        cursor.close()
        # conn.close()
    except Exception as e:
        print("Exception: ", e)
    return render_template('index.html', data=data_get)


def post_update():
    global data_update
    try:
        cursor = conn.cursor()
        # SQL statement to update te table
        update_query = """
        UPDATE genhubrequest
        SET status = %s WHERE requestid = %s;
        """
        # data_to_update=(data_to_be_updated,constraint_of_requestid)
        data_to_update = ("fail", "petergabriel@email.net_1718367059812")
        cursor.execute(update_query, data_to_update)
        conn.commit()

        cursor.execute("select * from genhubrequest;")
        data_update = cursor.fetchall()
        cursor.close()
        # conn.close()
    except Exception as e:
        print("Exception: ", e)
    return render_template('index.html', data=data_update)

def post_insert():
    # TODO Testing inserts
    # insert into genhubrequest (userid,request_time,requestid,requested_samples,available_samples,payable,status) select userid,'2024-09-24 18:22:13','prueba1@gmaila.com_1727198533767',requested_samples,available_samples+requested_samples,True,'rollbacking' from genhubrequest where requestid = 'prueba1@gmaila.com_1724414549546';
    pass


@app.route('/')
def index():
    # return 'Hello , we are in genhub request'
    return get_genhubrequest()

@app.route('/update')
def add():
    # return 'Hello , we are in genhub request'
    return post_update()


@app.route('/insert')
def insert():
    # return 'Hello , we are in genhub request'
    return post_insert()