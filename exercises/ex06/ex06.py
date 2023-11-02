import json

with open("nobel.json") as f:
    j = json.load(f)

d2 = {}

for d in j:
    if not d["awardLabel"] in d2:
        d2[d["awardLabel"]] = {"women": 0, "tot_winners": 0, "ages": []}
    d2[d["awardLabel"]]["tot_winners"] += 1
    age = int(d["date"].split("-")[0]) - int(d["birthDate"].split("-")[0])
    d2[d["awardLabel"]]["ages"].append(age)
    if d["sexLabel"] == "female":
        d2[d["awardLabel"]]["women"] += 1

out = {}
for a in d2:
    out[a] = {
        "percentageWomen": d2[a]["women"]/d2[a]["tot_winners"] * 100,
        "averageAge": sum(d2[a]["ages"]) / len(d2[a]["ages"])}

with open("stats.json", "w") as f:
    json.dump(out, f, indent=4)