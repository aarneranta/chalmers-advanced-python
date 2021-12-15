import json

# Question 1 #################################################################
def q1(path="nobel.json"):
    with open(path) as file:
        nobel = json.load(file)
    keys = set([it["awardLabel"] for it in nobel])
    
    def winners(award):
        return list(filter(lambda it: it["awardLabel"] == award, nobel))
    
    def women(winners):
        return list(filter(lambda it: it["sexLabel"] == "female", winners))

    def date(winner, birth=False):
        return int(winner["date" if not birth else "birthDate"].split("-")[0])

    new_dict = {}
    for key in keys:
        new_dict[key] = {}
        winnerlist = winners(key)
        percent_women = len(women(winnerlist)) / len(winnerlist) * 100
        new_dict[key]["percentageWomen"] = percent_women

        ages = [date(winner) - date(winner, birth=True) for winner in winnerlist]
        new_dict[key]["averageAge"] = int(sum(ages) / len(winnerlist))
    
    with open("nobel-statistics.json", "w") as file:
        json.dump(new_dict, file)

# Question 2 #################################################################
import matplotlib.pyplot as plt

def pie(labels, percents, title=""):
    fig = plt.figure()
    # to manually set colors
    # colors = ["orange", "blue"]
    # plt.pie(percents, labels = labels, colors = colors)
    plt.title(title)
    fig.savefig(title.replace(" ", "_") + ".pdf", format="pdf", dpi=fig.dpi)
    return plt

def plot_women_percents(path="nobel-statistics.json"):
    with open(path) as file:
        stats = json.load(file)
    for (key,val) in stats.items():
        women = val["percentageWomen"]
        pie(["women", "men"], [women, 100 - women], title=key)
    
# Question 3 #################################################################
import sys
sys.path.append("../../examples")
from trees import Graph
from hypothesis import example, given, strategies as st

twoints = st.tuples(st.integers(), st.integers())
st_edge_list = st.lists(twoints, unique_by=(lambda x: x[0], lambda x: x[1]))

def complete(G):
    nodes = G.vertices()
    edges = G.edges()
    for node in nodes:
        dests = []
        for (src,dst) in edges:
            if src == node:
                dests.append(dst)
            elif dst == node:
                dests.append(src)
            else:
                pass
        if set(nodes) != set(dests + [node]):
            return False
    return True

def easy_complete(G):
    n = len(G.vertices())
    return len(G.edges()) == (n*(n-1)) // 2

@given(st_edge_list)
def test_completeness(edges):
    G = Graph() 
    for (src,dst) in edges:
        if src != dst:
            G.add_edge(src, dst)
    assert easy_complete(G) == complete(G)


if __name__ == "__main__":
    test_completeness()