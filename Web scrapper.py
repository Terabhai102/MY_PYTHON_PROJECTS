# web scrapper
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def get_simple_info(query):
    # 1. Google se link dhundo
    print("Searching...")
    url = next(search(query, num_results=1))
    print(f"Fetching data from: {url}")
    
    # 2. Website ka data lao
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Sirf paragraph (p) tags ka text nikalo
    paragraphs = soup.find_all('p')
    
    # 4. Pehle 3 paragraphs ko display karo
    for p in paragraphs[:3]:
        print(p.text.strip())

# User input
topic = input("Kiske baare mein jaanna hai? ")
get_simple_info(topic)

    
        





























