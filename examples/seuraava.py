import urllib.parse as up

url_example = 'https://translate.google.com/?sl=en&tl=sv&text=what%20is%20this&op=translate'

url_parsed = up.urlparse(url_example)

print(url_parsed)


import requests as r

request_example = r.get(url_example)

print(request_example.status_code)
text = request_example.text


tramnetwork = 'https://www.wikidata.org/wiki/Q2297227'
tj = 'https://www.wikidata.org/wiki/Special:EntityData/Q2297227.json'
tr = r.get(tj)
print(tr.text)
