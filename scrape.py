from bs4 import BeautifulSoup
import urllib.request

source = urllib.request.urlopen('https://www.pgatour.com/stats/stat.02674.html').read()

soup = BeautifulSoup(source, 'lxml')

#for div in soup.find_all('div', class_='details-table-wrap'):
#    print (div.text)

table = soup.find('table', class_='table-styled')

table_rows = table.find_all('tr')

for tr in table_rows:
    th = tr.find_all('th')
    header = [i.text for i in th]
    print(header)
    break

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    rstrip(row)
    print(row)
