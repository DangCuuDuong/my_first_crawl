import requests
from bs4 import BeautifulSoup

url = "https://www.formula1.com/en/results/2024/drivers"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Page Title:", soup.title.text)  # Print the page title

    # Locate the table
    table = soup.find('table', class_="f1-table f1-table-with-data w-full")
    
    if table:
        # Extract all rows
        rows = table.find_all('tr')
        print(f"Found {len(rows)} rows in the table.")

        # Loop through rows to extract data
        for row in rows:
            cells = row.find_all('td')
            cell_texts = [cell.get_text(strip=True) for cell in cells]
            print(cell_texts)

