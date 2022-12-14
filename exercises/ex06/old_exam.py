# 2022-01-10

def tuples2dict(tuples):
    return {key: val for (key,val) in tuples}

lambda s1, s2: s1 if len(s1) >= len(s2) else s2

countries = {
"Afghanistan": {"capital": "Kabul", "area": 652230, "population":
36643815, "continent": "Asia", "currency": "afghani"},
"Albania": {"capital": "Tirana", "area": 28748, "population": 3020209,
"continent": "Europe", "currency": "lek"},
"Algeria": {"capital": "Algiers", "area": 2381741, "population":
41318142,
"continent": "Africa", "currency": "dinar"}
}

print(len({countries[c]["continent"] for c in countries}))


areas = {countries[c]["continent"]: 0 for c in countries}
for c in countries:
    areas[countries[c]["continent"]] += countries[c]["area"]
print(sorted(areas.items(), key=lambda p: p[1], reverse=True))

q5 = {
    1: [2,3,4],
    2: [1,3,4],
    3: [1,2],
    4: [1,2]
}

class Publication:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
 
    def publication_type(self):
        return 'publication'

class Book(Publication):
    def __init__(self, title, author, publisher=None):
        super().__init__(title, author) 
        self._publisher = publisher

    def get_publisher(self):
        return self._publisher

    def publication_type(self):
        return 'book'

class Article(Publication):
    def __init__(self, title, author, journal=None):
        super().__init__(title, author)
        self._journal = journal

    def get_journal(self):
        return self._journal

    def publication_type(self):
        return 'article'

fight = Book('Why Men Fight', 'Russell', 'The Century Co')
object = Book('Word and Object', 'Quine', 'MIT Press')
denoting = Article('On Denoting', 'Russell', 'Mind')
euro50 = Publication('50 euro banknote', 'European Central Bank')