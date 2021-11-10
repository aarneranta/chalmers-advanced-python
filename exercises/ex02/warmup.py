# Some simpler things that were shown in the first 10 minutes
# in a better format

# Reading files ##############################################################

# these two functions do the same thing:
def read1(path):
    f = open(path,"r") # read mode, can be omitted while write mode can't
    content = f.read()
    f.close() # do not forget!
    return content

def read2(path):
    with open(path) as f: # no need to explicitly close
        lines = f.read()
    return lines

# For loops vs comprehensions ################################################

# these two functions also do the same thing!
def for1():
    list = ["a", "b", "c"]
    list2 = []
    for el in list:
        list2.append(el.upper())
    return list2

def for2():
    list = ["a", "b", "c"]
    return [el.upper() for el in list] 