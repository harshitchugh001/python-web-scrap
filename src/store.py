from config.db_config import connect_db
import psycopg2
import re

def create_database(cursor):
    try:
        cursor.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname = 'harshit_scrap'")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE harshit_scrap")
            print("Database 'harshit_scrap' created")
        else:
            print("Database 'harshit_scrap' already exists")
    except psycopg2.Error as e:
        print(f"Error creating database: {e}")



def store_properties(properties):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        create_database(cursor)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                price VARCHAR(255),
                size VARCHAR(20),
                location VARCHAR(255),
                status VARCHAR(50),
                url VARCHAR(255)
            )
        """)
        print("Table 'properties' created or already exists")

        for prop in properties:
            print(prop)
            
            # price = preprocess_price(prop['price'])
            cursor.execute("""
                INSERT INTO properties (title, price, size, location, status, url)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    prop['title'], prop['price'], prop['size'],
                    prop['location'], prop['status'], prop['url']
                ))
        conn.commit()
        print("Properties have been successfully stored in the database")

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()




def preprocess_price(price_str):
   
    match = re.search(r'₹([\d.]+) Lac', price_str)
    if match:
        price = float(match.group(1)) * 100000 
        return price
    else:
        return None




def store_presidents(presidents):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        create_database(cursor)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS presidents (
                id SERIAL PRIMARY KEY,
                Name VARCHAR(255),
                Dates VARCHAR(255),
                Nationality VARCHAR(255),
                Previouswork VARCHAR(255)
            )
        """)
        print("Table 'presidents' created or already exists")

        sample = []

        for prop in presidents:
            # print("prop",prop)
            if prop == presidents[0]:
                continue
            name, dates, nationality, previous_work = prop
            
            sample.append({"name": name, "dates": dates, "nationality": nationality, "previous_work": previous_work})  

        # print(sample)
                        
        for i in sample:    
            cursor.execute("""
                INSERT INTO presidents (Name, Dates, Nationality, previouswork)
                VALUES (%s, %s, %s, %s)
                    """, (
                    i['name'], i['dates'], i['nationality'],
                    i['previous_work']
                ))
        conn.commit()
        print("Presidents have been successfully stored in the database")

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()
    