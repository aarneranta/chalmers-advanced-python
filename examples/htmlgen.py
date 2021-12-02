# a simple library for generating well-formatted HTML code

def intag(tag, elems, attrs='', newline=False):
    """
    Creates a HTML element by wrapping a list of elements between a start and end tag, 
    optionally adding newlines.
    """
    a = ' ' if attrs else ''
    n = '\n' if newline else ''
    return '<'+tag+a+ attrs+'>' + n + '\n'.join(elems) + n + '</'+tag+'>'


def attrs(dict):
    # forms an attribute list from a dictionary
    ats = []
    for k in dict:
        ats.append(str(k) + '=' + '"' + str(dict[k]) + '"')
    return ' '.join(ats)

def newintag(tag, elems, attrs=''):
    "Builds element with intag with newlines always added."
    return intag(tag, elems, attrs, newline=True)


def html(head, body):
    "Generates a complete HTML document from a head and a body lists of elements."
    return '<!DOCTYPE html>\n' + newintag('html',[newintag('head', head), newintag('body', body)])


def title(s):
    "Generates a title from a string."
    return intag('title', [s])


def h1(s):
    "Generates a heading of level 1 from a string."
    return intag('h1', [s])


def p(s):
    "Generates a paragraph from a list of strings."
    return intag('p', [s])


def a(url, s):
    "Generates a hypertag from a URL and an element."
    return intag('a', [s], attrs=attrs({'href': url}))


def table(th, data):
    "Generates a table from a list of header names and a list of data lists."
    return newintag(
        'table', [
        newintag('tr', [intag('th',[e]) for e in th])
           ] + [
        newintag('tr', [intag('td',[e]) for e in d]) for d in data]
                        )


# example table showing powers of numbers
powertable = table (
    ['x**' + str(n) for n in range(1,10)],
    [[str(x**10) for n in range(1,10)] for x in range(1,101)]
    )


# a simple document illustrating functions in this module
doc = html(
        [title('Example')],
        [h1('First example'),
         p('This is an example.'),
         powertable,
         a('https://chalmers.instructure.com/courses/15902', 'course web page')
        ])


if __name__ == '__main__':
    print(doc)


