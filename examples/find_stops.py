"""
Find the URLs of Västtrafik traffic information pages for each tram stop.
"""

from bs4 import BeautifulSoup
import json
from requests import get

url = 'https://www.vasttrafik.se/reseplanering/hallplatslista/'

doc = get(url, verify=False)

soup = BeautifulSoup(doc.text, 'html.parser')


# stop_prefix = 'https://www.vasttrafik.se'
stop_prefix = 'https://avgangstavla.vasttrafik.se/?source=vasttrafikse-stopareadetailspage&stopAreaGid='
# print all links and the texts that link to them

#for link in soup.find_all('a'):
#    print(link.text, link.get('href'))


# another useful task: print just the text, no tags
# print(soup.get_text())  


stopdict = {}
for link in soup.find_all('a'):
    stop = link.text.split(',')
    id = link.get('href')
    prefixlen = len('/reseplanering/hallplatser/')
    if id.startswith('/reseplanering/hallplatser/') and len(stop)==3:
        name, town, _ = stop[:3]
        stopdict[name.strip() + ';' + town.strip()] = stop_prefix + id[prefixlen:-1]

print(json.dumps(stopdict, indent=2, ensure_ascii=False))

