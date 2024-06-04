from src.scrape import scrape_properties
from src.store import store_properties,store_presidents
from src.export import generate_csv,generate_csv_presidents
from src.scrape import scrape_worldbank



def main():
    properties = scrape_properties()  
    for property in properties:
        print(property)
    
    presidents = scrape_worldbank()
    
    for president in presidents:
        print(president)
        
    store_presidents(presidents)
    
    
    
    store_properties(properties)  
    generate_csv() 
    generate_csv_presidents()

if __name__ == "__main__":
    main()
