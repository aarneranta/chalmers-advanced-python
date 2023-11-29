import matplotlib.pyplot as plt
import json

def show_pie_chart(distr_dict, title=""):
    labels = []
    percents = []
    for (label,percent) in distr_dict.items():
        labels.append(label)
        percents.append(percent)
    plt.pie(percents, labels=labels)
    plt.title(title)
    plt.show() 

def show_nobel_pie_chart(stats_dict_path="stats.json"):
    with open(stats_dict_path) as f:
        stats_dict = json.load(f)
    for award in stats_dict:
        percent_women = stats_dict[award]["percentageWomen"]
        new_dict = {"women": percent_women, "men": 100 - percent_women}
        show_pie_chart(new_dict, title=award)



if __name__ == "__main__":
    show_nobel_pie_chart()
