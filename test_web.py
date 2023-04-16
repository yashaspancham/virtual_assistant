import requests
from bs4 import BeautifulSoup

# Ask for user input for search query
search_query = input("What do you want to search on Google? ")

# Google search URL format
url = "https://www.google.com/search?q=" + search_query

# Send request to Google and get response
response = requests.get(url)


# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, "html.parser")


# Find all search results
search_results = soup.find_all("div")
print(search_results)
# Print the titles and URLs of the search results
for result in search_results[:10]:
    try:
        title = result.find("h3").get_text()
        url = result.find("a")["href"]
        print(title + ": " + url)
    except:
        pass
