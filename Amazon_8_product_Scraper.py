import requests
from bs4 import BeautifulSoup

# Set the URL of the page you want to scrape
url = "https://www.amazon.com/s?k=product1+product2+product3+product4+product5+product6+product7+product8"

# Make a request to the page
page = requests.get(url)

# Create a Beautiful Soup object
soup = BeautifulSoup(page.text, "html.parser")

# Find all the elements on the page with the class "s-result-item"
results = soup.find_all("div", class_="s-result-item")

# Loop through the results and print the prices
for result in results:
  # Find the element with the class "a-offscreen"
  price_element = result.find("span", class_="a-offscreen")
  
  # If the element was found, print the text
  if price_element:
    print(price_element.text)
  # If the element was not found, print "Price not found"
  else:
    print("Price not found")
