# a simple library for generating well-formatted HTML code

class Tree:
    "HTML elements as trees (or XML, since no tagset is assumed)."
    def __init__(self, tag, elems, attrs=None, newlines=True):
        self._tag = tag
        self._elems = elems
        self._attrs = attrs
        self._newlines = newlines

    def render(self):
        if attrs := self._attrs:
            attrs = f" {' '.join([f'{key}={value}' for key, value in attrs.items()])}"
        else:
            attrs = ""
        start = '<' + self._tag + attrs + '>'
        end = '</'+ self._tag + '>'
        sep = '\n' if self._newlines else ''
        
        def renders(elem):
            return elem.render() if isinstance(elem, Tree) else str(elem)
        
        content = sep.join([renders(e) for e in self._elems])
        return sep.join([start, content, end])


def intag(tag, parts, attrs=None, newlines=True):
    """
    Creates a HTML element by wrapping a given element
    or a list of elements or strings
    between a start tag and matching end tag, 
    optionally adding newlines.
    """
    if isinstance(parts, list):
        return Tree(tag, parts, attrs, newlines)
    else:
        return Tree(tag, [parts], attrs, newlines)


def b(s):
    "Generates a boldfaced text from a string."
    return intag('b', s, newlines=False)


def p(ss):
    "Generates a paragraph from a string or a list of elements."
    return intag('p', ss)


def a(url, s):
    "Generates a hypertag from a URL and an element."
    return intag('a', s, attrs={'href': url}, newlines=False)


def html(head, body):
    "Generates a complete HTML document from a head and a body lists of elements."
    # return '<!DOCTYPE html>\n' +
    return intag('html',
                 [intag('head', head),
                   intag('body', body)],
                 attrs={'xmlns': "http://www.w3.org/1999/xhtml"})


def title(s):
    "Generates a title (for a head) from a string."
    return intag('title', s, newlines=False)


def h1(s):
    "Generates a heading of level 1 from a string."
    return intag('h1', s, newlines=False)


def table(th, data, border=1):
    "Generates a table from a list of header names and a list of data lists."
    return intag(
        'table',
        [intag('tr', [intag('th', e, newlines=False) for e in th])] +
        [intag('tr', [intag('td', e, newlines=False) for e in d]) for d in data],
        attrs = {'border': str(border)}
        )


# a document about Gbg trams
import json

TRAMDOC = 'tramnetwork.json'  # your Lab 1 generated JSON file

def tramdoc():
    with open(TRAMDOC) as data:
        tramdata = json.load(data)
    lines = tramdata['lines'].items()
    linetable = table (
        ['line', 'stops'],
        [[line, ', '.join(stops)] for line, stops in lines]
        )
    return html(
        [intag('meta', [], attrs={'charset': "UTF-8"})],
        [
            h1('The Tram Lines of Gothenburg'),
            p(
                ['For timetables, see ',
                 a('https://www.vasttrafik.se/en/', 'Västtrafik')
                ]
              ),
            linetable
        ]
      )

koe = b(a('https://www.vasttrafik.se/en/', b('Västtrafik')))

if __name__ == '__main__':
    print(tramdoc().render())
#    print(koe.render())


