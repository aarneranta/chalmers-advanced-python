# Question 1
def norway_pandemic():
    region = input("Hvor er du bosatt? ")
    if region[0] == "V" or region[1] == "V":
        # bonus: try to avoid repetition by writing a function that handles 
        # all yes/no questions
        print("Velkommen til Norge!")
        return
    vaccine = input("Er du fullvaksinert?")
    if vaccine == "ja":
        print("Velkommen til Norge!")
        return
    covid = input("Har du gjennomgått koronasykdom de siste seks månedene?")
    if covid == "ja":
        print("Velkommen til Norge!")
        return
    else:
        print("Velkommen til Norge, men du må teste deg och sitte i karantene.")

# Question 2
def price(drinks):
    prices = [("kaffe", 30), ("öl", 50), ("kola", 25)]
    [n, name] = drinks.split()
    for (s, price) in prices:
        if s == name:
            return price * int(n)
    return 0

def get_order():
    drink = input("Vad vill ni dricka?")
    total = 0
    while drink != "Det är bra så":
        p = price(drink)
        if p == 0:
            print("Finns tyvärr inte")
        total += p
        drink = input("Något mer?")
    print("Det blir", total, "kronor")

# Question 3
def alter(s):
    if len(s) < 2:
        return s
    else:
        return s[1] + s[0] + alter(s[2:])

def scramble(s):
    if len(s) < 2:
        return s
    return s[0] + alter(s[1:-1]) + s[-1]

def scrambles(s):
    words = s.split()
    scrambled_words = []
    for word in words:
        scrambled_words.append(scramble(word))
    return " ".join(scrambled_words)

# Question 4
edges = [(0,1), (1,2), (2,0), (2,3)]

def edges2adjacency(edges):
    d = {}
    # bonus: try to make this for loop more compact
    for (src, trg) in edges:
        if src in d:
            d[src].append(trg)
        else:
            d[src] = [trg]
        if trg in d:
            d[trg].append(src)
        else:
            d[trg] = [src]
    return d

# bonus: try to do this with a single list comprehension
def adjacency2edges(adj):
    edges = []
    for (src, trgs) in adj.items():
        for trg in trgs:
            if (src,trg) not in edges and (trg,src) not in edges:
                edges.append((src,trg))
    return edges
