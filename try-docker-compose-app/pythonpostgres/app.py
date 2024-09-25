import os
from typing import List, Any
import psycopg2
from datetime import datetime
from flask import Flask, render_template

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
browse_query = "select * from genhubrequest;"
conn = psycopg2.connect(host=db_hostname, user=db_username, password=passwd, port=port, dbname="genhub")


def timestamp_in_millis():
    now = datetime.now()
    timestamp = round(datetime.timestamp(now) * 1000)
    return timestamp


def get_genhubrequest():
    data_get = list[Any]
    try:
        cur = conn.cursor()
        cur.execute(browse_query)
        # for record in cursor:
        #   print(record)
        data_get = cur.fetchall()
        cur.close()
        # conn.close()
    except Exception as e:
        print("Exception: ", e)
    return render_template('index.html', data=data_get)


def post_update():
    data_update = list[Any]
    try:
        cur = conn.cursor()
        # SQL statement to update te table
        update_query = """
        UPDATE genhubrequest
        SET status = %s WHERE requestid = %s;
        """
        # data_to_update=(data_to_be_updated,constraint_of_requestid)
        data_to_update = ("fail", "petergabriel@email.net_1718367059812")
        cur.execute(update_query, data_to_update)
        conn.commit()
        cur.execute(browse_query)
        data_update = cur.fetchall()
        cur.close()
    except Exception as e:
        print("Exception: ", e)
    return render_template('index.html', data=data_update)


def post_insert():
    now_formatted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    request_id = "petergabriel@email.net_1718367059812"
    user_id = "petergabriel@email.net"
    request_id_new = f"{user_id}_{timestamp_in_millis()}"
    data_insert = List[Any]
    try:
        query = (
            f"insert into genhubrequest (userid,request_time,requestid,requested_samples,available_samples,payable,"
            f"status) select userid,'{now_formatted}','{request_id_new}',requested_samples,"
            f"available_samples+requested_samples,"
            f"True,'rollbacking' from genhubrequest where requestid = '{request_id}';")
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.execute(browse_query)
        data_insert = data_insert = cur.fetchall()
        cur.close()
    except Exception as err:
        print("Exception: ", err)
    finally:
        pass
        # if conn:
        #    conn.close()
    return render_template('index.html', data=data_insert)


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
