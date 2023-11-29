import json 

if __name__ == "__main__":
    with open("nobel.json") as f:
        jobj = json.load(f)

    stats_dict = {}

    for winner in jobj:
        year_won = int(winner["date"][:4])
        year_born = int(winner["birthDate"][:4])
        age = year_won - year_born
        if winner["awardLabel"] not in stats_dict.keys():
            stats_dict[winner["awardLabel"]] = {
                "percentageWomen": [1 if winner["sexLabel"] == "female" else 0, 1],
                "averageAge": [age]}
        else: 
            if winner["sexLabel"] == "female":
                stats_dict[winner["awardLabel"]]["percentageWomen"][0] += 1
            stats_dict[winner["awardLabel"]]["percentageWomen"][1] += 1 
            stats_dict[winner["awardLabel"]]["averageAge"].append(age)
    
    for award in stats_dict:
        stats_dict[award]["percentageWomen"] = round((stats_dict[award]["percentageWomen"][0] / stats_dict[award]["percentageWomen"][1]) * 100, 2)
        stats_dict[award]["averageAge"] = round(sum(stats_dict[award]["averageAge"]) / len(stats_dict[award]["averageAge"]), 2)

    with open("stats.json", "w") as f:
        json.dump(stats_dict, f, indent=1)