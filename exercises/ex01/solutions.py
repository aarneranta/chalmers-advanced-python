def yes_no_quest(question_string):
    answer = input(question_string)
    if answer == "ja":
        print("Velkommen til Norge!")
        exit(0)

def norway_pandemic():
    place = input("Hvor er du bosatt?" )
    if place[0] == "V":
        print("Velkommen til Norge!")
        exit(0)
    yes_no_quest("Er du fullvaksinert?" )
    yes_no_quest("Har du gjennomgått koronasykdom de siste seks månedene? " )
    print("Velkommen til Norge, men du må teste deg och sitte i karantene.")
    exit(0)
    
price_list = [("kaffe", 30), ("öl", 50), ("kola", 25)]

def price(string): # string: 4 kaffe
    [number, name] = string.split(" ") #split(string, " ")
    for item in price_list:
        if name == item[0]:
            return item[1] * int(number)
    return 0

def get_order():
    total = 0
    order = input("Vad vill ni dricka? ")
    while (order != "Det är bra så"):
        part_price = price(order)
        if part_price != 0:
            total += part_price
        else:
            print("Finns tyvärr inte")
        order = input("Något mer?")
    print("Det blir " + str(total) + " kronor")
        
test_str = "According to a researcher at Cambridge University , it doesn't matter in what order the letters in a word are , the only important thing is that the first and last letter be at the right place."

def alter(s):
    if len(s) < 2:
        return s
    if len(s) == 2:
        return s[-1] + s[0]
    else:
        return alter(s[:2]) + alter(s[2:])

def scramble(s):
    if len(s) < 2:
        return s
    return s[0] + alter(s[1:-1]) + s[-1]

def scrambles(s):
    # divide into words
    words = s.split(" ")
    # apply scramble to each
    scrambled_words = []
    for word in words:
        scrambled_words.append(scramble(word)) # append(scrambled_words, scrambled(word))
    # concate scrambled words
    return " ".join(scrambled_words)

edges = [(0,1), (1,2), (2,0), (2,3)]

def edges2adjacency(edges):

    def add_edge(adj,src,dst):
        if not src in adj:
            adj[src] = [dst]
        else:
            adj[src].append(dst)

    adj = {}
    for (src,dst) in edges:
        add_edge(adj, src, dst)
        add_edge(adj, dst, src)
    
    return adj

def adjacency2edges(adj):
    edges = []
    for (src,dsts) in adj.items():
        for dst in dsts:
            if not (src,dst) in edges and not (dst,src) in edges: 
                edges.append((src,dst))
    return edges


    


