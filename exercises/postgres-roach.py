'''
# Connect dialog on cocroach labs has the following instructions
curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/8cabf4f1-a1d1-4053-ad0b-2ae3b93b2f9f/cert'

export DATABASE_URL="postgresql://binu:SECRET_TOKEN@tunnel-chinook-6809.g8z.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"

!pip install psycopg2-binary

CREATE DATABASE binu1;
CREATE TABLE binu1.CUSTOMER1(cid serial PRIMARY KEY,
	cust_name VARCHAR ( 50 ) UNIQUE NOT NULL,
	homeurl VARCHAR ( 255 ) UNIQUE NOT NULL, 
	active BOOLEAN DEFAULT false, effective DATE, created_on TIMESTAMP NOT NULL);

'''

import os
import psycopg2
import datetime

def print_version(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        res = cur.fetchall()
        conn.commit()
        print("Version is below:")
        print(res)

def print_datetime(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT now()")
        res = cur.fetchall()
        conn.commit()
        print("Time Now is below:")
        print(res)

def create(conn):
    with conn.cursor() as cur:
        # SQL query to create a new table
        create_table_query = '''CREATE TABLE IF NOT EXISTS
            ITEM
            (ID           INT PRIMARY KEY     NOT NULL,
            MODEL         TEXT    NOT NULL,
            ACTIVE        BOOL DEFAULT TRUE,
            PRICE         REAL); '''
        # Execute a command: this creates a new table
        cur.execute(create_table_query)
        conn.commit()
        print("Table ITEM created successfully in PostgreSQL ")

def insertIfNotExists(conn):
    with conn.cursor() as cur:
        somecustid = "Customer3"
        cur.execute(
        """
        SELECT c.cust_name 
        FROM binu1.CUSTOMER1 c
        WHERE c.cust_name = %s;
        """,
        [somecustid,]
        )
        result = cur.fetchone()
        print(f"result of fetch:{result}")

        if result is None:
            cur.execute("""
            INSERT INTO binu1.CUSTOMER1(cust_name, homeurl, active, effective, created_on) 
            VALUES (%s, %s, %s, %s, %s);
            """,
            (somecustid, "www.customer3.com",True, datetime.date(2023, 11, 18), datetime.datetime.now()))
            conn.commit()
            print(f"Inserted record for {somecustid}")
        else:
            print(f"Record already exists for {somecustid}")

def getCustDate(custN):
    return datetime.date(custN["start"]["year"], custN["start"]["month"], custN["start"]["day"])
                  
def insertIfNotExistsWithDict(conn, custN):
    with conn.cursor() as cur:
        cur.execute(
        """
        SELECT c.cust_name 
        FROM binu1.CUSTOMER1 c
        WHERE c.cust_name = %s;
        """,
        [custN["name"],]
        )
        result = cur.fetchone()
        print(f"result of fetch:{result}")

        if result is None:
            cur.execute("""
            INSERT INTO binu1.CUSTOMER1(cust_name, homeurl, active, effective, created_on) 
            VALUES (%s, %s, %s, %s, %s);
            """,
            (custN["name"], custN["url"], (custN['status']=="Y"), getCustDate(custN), datetime.datetime.now()))
            conn.commit()
            print(f"Inserted record for {custN['name']}")
        else:
            print(f"Record already exists for {custN['name']}")

def main():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    print_version(conn)
    print_datetime(conn)
    create(conn)
    insertIfNotExists(conn)
    
    cust1 = {
        "name": "Customer6",
        "url": "www.customer6.com",
        "status": "N",
        "start": { "year": 2023, "month": 10, "day":22}
    }
    insertIfNotExistsWithDict(conn,cust1)

if __name__ == '__main__':
    main()
