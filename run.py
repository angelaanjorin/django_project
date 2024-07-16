import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://gmedical.com/blog/love-and-locums/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all paragraphs
paragraphs = soup.find_all('p')

# Extract the text content from each paragraph and join them into a single string
text_content = "\n\n".join([para.get_text() for para in paragraphs])

# Print the extracted text content
print(text_content)
