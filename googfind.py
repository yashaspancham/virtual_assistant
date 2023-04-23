import webbrowser
from googlesearch import search
import sys
import re

def googfind(said):
    if re.search(r'Google.*', said):
        # Define the search query
        query = said
        # Perform Google search and open 3 search results in web browser
        number_of_results = 1
        for j in search(query):
            if number_of_results >= 3 and number_of_results <= 5:
                print(f"Opening the URL: {j}")
                webbrowser.open(j)
                number_of_results += 1
            elif number_of_results < 3:
                number_of_results += 1
            else:
                sys.exit()
                break

