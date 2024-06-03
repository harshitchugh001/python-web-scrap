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
