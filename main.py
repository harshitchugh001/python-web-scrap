from src.scrape import scrape_properties
from src.store import store_properties, store_presidents
from src.export import generate_csv, generate_csv_presidents
from src.scrape import scrape_worldbank
from src.crud import insert_property, delete_property, update_property, read_properties

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

    while True:
        print("\nCRUD Menu:")
        print("1. Insert Property")
        print("2. Update Property")
        print("3. Delete Property")
        print("4. Read Properties")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            property = {
                'title': input("Enter title: "),
                'price': input("Enter price: "),
                'size': input("Enter size: "),
                'location': input("Enter location: "),
                'status': input("Enter status: "),
                'url': input("Enter URL: ")
            }
            insert_property(property)
            
        elif choice == '2':
            property = {
                'id': input("Enter the ID of the property to update: "),
                'title': input("Enter new title: "),
                'price': input("Enter new price: "),
                'size': input("Enter new size: "),
                'location': input("Enter new location: "),
                'status': input("Enter new status: "),
                'url': input("Enter new URL: ")
            }
            update_property(property)
            
        elif choice == '3':
            property_id = input("Enter the ID of the property to delete: ")
            delete_property(property_id)
            
        elif choice == '4':
            read_properties()
            
        elif choice == '5':
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
