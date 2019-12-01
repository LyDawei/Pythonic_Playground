import requests
import csv
from bs4 import BeautifulSoup

url = 'https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s?max_rows=500'


def writeToFile(data):
    print('Writing data to file.')
    outfile = open('./inmates.csv', 'w', newline='')
    writer = csv.writer(outfile)
    writer.writerow([
        "Last",
        "First",
        "Middle",
        "Suffix",
        "Sex",
        "Race",
        "Age",
        "City",
        "State"])
    writer.writerows(data)
    print('Writing data to file complete.')


def scrape():
    print('Scraping data...')
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = response.content
    soup = BeautifulSoup(html, features='html.parser')
    table = soup.find('tbody', attrs={'class': 'stripe'})
    list_of_rows = []
    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text\
                .replace('&nbsp;', '')\
                .replace('''\n''', '')\
                .replace('''\xa0''', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    print('Scaping complete')
    writeToFile(list_of_rows)


if __name__ == "__main__":
    print(''' Executing Scraper program. ''')
    scrape()
    print(''' Scraper program finished. ''')
