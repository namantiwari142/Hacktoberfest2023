import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find and extract specific elements from the page
    articles = soup.find_all('article')
    
    # Loop through the articles and extract their titles
    for article in articles:
        title = article.find('h2').text if article.find('h2') else "No title available"
        print(f"Article Title: {title}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
