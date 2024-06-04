import requests
from bs4 import BeautifulSoup

def scrape_properties():
    url = "https://www.magicbricks.com/property-for-sale-rent-in-Chandigarh/residential-real-estate-Chandigarh"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    properties = []

    for listing in soup.find_all('div', class_='mb-home__owner-prop__card'):
        title = listing.find('div', class_='mb-home__owner-prop__card--type').text.strip()
        price = listing.find('div', class_='mb-home__owner-prop__card--price').text.strip()
        size = listing.find('span', class_='mb-home__owner-prop__card--size').text.strip() if listing.find('span', class_='mb-home__owner-prop__card--size') else 'N/A'
        location = listing.find('div', class_='mb-home__owner-prop__card--loc').text.strip()
        status = listing.find('div', class_='mb-home__owner-prop__card--status').text.strip()
        url = listing.find('a')['onclick'].split("',")[1].split("'")[1]

        properties.append({
            'title': title,
            'price': price,
            'size': size,
            'location': location,
            'status': status,
            'url': url
        })

    return properties



def scrape_worldbank():
    url = "https://en.wikipedia.org/wiki/World_Bank"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # print(soup)
    presidents = []
    
    table = soup.find('table', {'class': 'wikitable'})
    
    # print(table)
    
    rows = table.find_all('tr')


    headers = [header.text.strip() for header in rows[0].find_all('th')]


    presidents.append(headers)
        
    for row in rows[1:]:
        columns = row.find_all('td')
        columns_data = [column.text.strip() for column in columns]
        presidents.append(columns_data)
        
    for president in presidents:
        print(president)


    return presidents