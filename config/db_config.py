import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="harshit_scrap",
            user="postgres",
            password="hhhhhh",
            host="localhost"
        )
        print("Successfully connected to the database")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
