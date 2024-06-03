import csv
from config.db_config import connect_db

def fetch_properties():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM properties")
    properties = cursor.fetchall()
    cursor.close()
    conn.close()
    return properties

def generate_csv(filename='data/properties.csv'):
    properties = fetch_properties()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'price', 'size', 'location', 'status', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for property in properties:
            writer.writerow({
                'id': property[0],
                'title': property[1],
                'price': property[2],
                'size': property[3],
                'location': property[4],
                'status': property[5],
                'url': property[6]
            })
        print("csv exported")
