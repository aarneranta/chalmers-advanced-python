from bs4 import BeautifulSoup

import urllib.request as ur
import requests as r

python_wikipedia_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# https://www.howtouselinux.com/post/ssl-certificate_verify_failed-in-python
doc = r.get(python_wikipedia_url, verify=False)

# with ur.urlopen(python_wikipedia_url) as doc:
soup = BeautifulSoup(doc.text, 'html.parser')

# print(soup.prettify())

#for link in soup.find_all('a'):
#    print(link.text, link.get('href'))

# print(soup.get_text())     

#for t in soup.find_all('p'):
#    print(t.text)


#tram_url = 'https://www.vasttrafik.se/reseplanering/hallplatslista/'




"""
import urllib.parse as up

url_example = 'https://translate.google.com/?sl=en&tl=sv&text=what%20is%20this&op=translate'

url_parsed = up.urlparse(url_example)

print(url_parsed)


request_example = r.get(url_example)

print(request_example.status_code)
text = request_example.text


tramnetwork = 'https://www.wikidata.org/wiki/Q2297227'
tj = 'https://www.wikidata.org/wiki/Special:EntityData/Q2297227.json'
tr = r.get(tj)
print(tr.text)
"""
