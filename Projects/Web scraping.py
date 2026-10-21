
# Import requests to retrieve webpages.
import requests

# Import BeautifulSoup to parse and search HTML.
from bs4 import BeautifulSoup

# Store the URL of the Wikipedia page we want to scrape.
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_South_Africa"

# Request the webpage and wait up to 15 seconds for a response.
# Identify the script and provide contact information if appropriate.
headers = {
    "User-Agent": "PythonLearningProject/1.0 (educational web scraping)"
}

# Send the request with the user-agent header.
page = requests.get(url, headers=headers, timeout=15)

# Check whether the request succeeded.
page.raise_for_status()

# Raise an error if the website returns an unsuccessful HTTP status.
page.raise_for_status()

# Parse the returned HTML using the specified HTML parser.
soup = BeautifulSoup(page.text, "html.parser")

# Print the page title so we can confirm which page was retrieved.
print(soup.title.get_text(strip=True) if soup.title else "No title found")

# Find all tables with the specified Wikipedia table classes.
world_tables = soup.find_all(
    "table",
    class_="wikitable sortable"
)

# Check whether at least two matching tables were found.
if len(world_tables) > 1:

    # Select the second matching table (index 1 means the second item).
    world_table = world_tables[1]

    # Find all column headings inside that table.
    world_titles = world_table.find_all("th")

    # Extract and clean the text from each column heading.
    world_table_titles = [
        title.get_text(strip=True)
        for title in world_titles
    ]

    # Print the extracted column headings.
    print(world_table_titles)

# Handle the case where fewer than two matching tables were found.
else:
    print("Fewer than two matching tables were found.")


#<table class="wikitable sortable jquery-tablesorter" id="mwGQ">

#</tbody><tfoot><tr class="mw-empty-elt" id="mwAe0"></tr></tfoot></table>