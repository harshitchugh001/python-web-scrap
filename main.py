from src.scrape import scrape_properties
from src.store import store_properties
from src.export import generate_csv


def main():
    properties = scrape_properties()  
    for property in properties:
        print(property)
    store_properties(properties)  
    generate_csv() 

if __name__ == "__main__":
    main()
