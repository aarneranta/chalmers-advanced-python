import json

# quick and dirty way to change links in our SVG IN_FILE

STOPID_FILE = 'stopids.json'  # your generated file


GOOGLE_FILE = 'tramstop_google_url.json'
SVG_IN_FILE = 'gbg_tramnet.svg'

GOOGLE_PREFIX = 'https://www.google.com/'

with open(GOOGLE_FILE) as file:
    googles = json.load(file)
    googles = {val: key for key, val in googles.items()}
 
with open(STOPID_FILE) as file:
    stopids = json.load(file)
 
url_changes = {google: stopids[stop] for google, stop in googles.items()}



# lines in SVG_IN_FILE to be changed have three parts
def change_line(line, changes):
    if (i := line.find(GOOGLE_PREFIX)) > 0:
        old_url = line[i:].split()[0][:-1]
        new_url = url_changes.get(old_url, 'foo').replace('&', '&amp;')
        return line.replace(old_url, new_url)
    else:
        return line


with open(SVG_IN_FILE) as file:
    for line in file:
        print(change_line(line, url_changes).strip())


