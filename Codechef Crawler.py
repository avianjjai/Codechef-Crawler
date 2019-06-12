from bs4 import BeautifulSoup as soup
import requests

website = "https://www.codechef.com"
context = "/contests"
filename ="Codechef competitions.csv"
f = open(filename,"w")

codechef = requests.get(website+context)
codechef_html = soup(codechef.content,"html.parser")
table_heading = ''
for th in codechef_html.thead.tr.find_all("th"):
    table_heading += th.text.strip() + ','
table_heading = table_heading+'Comptition Link'
f.write(table_heading+'\n')

for tbody in codechef_html.find_all("tbody")[:2]:
    for tr in tbody.find_all("tr"):
        table_data = ""        
        for td in tr.find_all("td"):
            table_data += td.text.strip() + ','
        table_data = table_data+website+tr.a.get("href")
        f.write(table_data+"\n")
f.close()
print('Done')