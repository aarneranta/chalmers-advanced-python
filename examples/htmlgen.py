# a simple library for generating well-formatted HTML code

def intag(tag, elems, attrs='', newlines=False):
    """
    Creates a HTML element by wrapping a list of elements
    between a start and end tag, 
    optionally adding newlines.
    """
    attrs = ' ' + attrs if attrs else ''
    new = '\n' if newlines else ''
    start = '<' + tag + attrs + '>'
    end = '</'+ tag + '>'
    content = new.join(elems)
    return new.join([start, content, end])


def b(s):
    "Generates a boldfaced text from a string."
    return intag('b', [s])


def linesintag(tag, elems, attrs=''):
    "Builds element with intag with newlines always added."
    return intag(tag, elems, attrs, newlines=True)


def p(ss):
    "Generates a paragraph from a list of strings."
    return linesintag('p', ss)


def attrs(dict):
    # forms an attribute list from a dictionary
    ats = []
    for k, v in dict.items():
        ats.append(str(k) + '=' + '"' + str(v) + '"')
    return ' '.join(ats)

def a(url, s):
    "Generates a hypertag from a URL and an element."
    return intag('a', [s], attrs=attrs({'href': url}))


def html(head, body):
    "Generates a complete HTML document from a head and a body lists of elements."
    return '<!DOCTYPE html>\n' + linesintag('html',
                      [linesintag('head', head),
                       linesintag('body', body)],
                      attrs='xmlns="http://www.w3.org/1999/xhtml"')


def title(s):
    "Generates a title (for a head) from a string."
    return intag('title', [s])


def h1(s):
    "Generates a heading of level 1 from a string."
    return intag('h1', [s])


def table(th, data):
    "Generates a table from a list of header names and a list of data lists."
    return linesintag(
        'table',
        [linesintag('tr', [intag('th',[e]) for e in th])] +
        [linesintag('tr', [intag('td',[e]) for e in d]) for d in data],
        attrs = attrs({'border': '1'}),
        )


# example table showing powers of numbers
powertable = table (
    ['x**' + str(n) for n in range(1,7)],
    [[str(x**n) for n in range(1,7)] for x in range(1,101)]
    )


# a simple document illustrating functions in this module
powerdoc = html(
        [title('Example')],
        [h1('First example'),
         p(['This is an', b('example'), 'paragraph.']),
         h1('Second example: a table'),
         powertable,
         h1('Third example: a link'),
         a('https://chalmers.instructure.com/courses/20986', 'course web page')
        ])


# a document about Gbg trams
import json

TRAMDOC = 'tramnetwork.json'

def tramdoc():
    with open(TRAMDOC) as data:
        tramdata = json.load(data)
    lines = tramdata['lines'].items()
    linetable = table (
        ['line', 'stops'],
        [[line, ', '.join(stops)] for line, stops in lines]
        )
    return html(['tramlines'], [linetable])


if __name__ == '__main__':
#    print(powerdoc)
    print(tramdoc())


