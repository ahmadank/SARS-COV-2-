import networkx as nx
import matplotlib.pyplot as plt
import csv

g=nx.Graph()
EU = ["Austria", "Belgium", "Bulgaria", "Croatia", 
"Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands"
, "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]
color_Map = []
node_Sizes =[]
with open('countries.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row["country_border_name"] == ""):
            g.add_node(row["country_name"])
        else:
            g.add_edge(row["country_name"],row["country_border_name"])
index = 0
for node in g:
    index += 1
    with open('EUCovid.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["location"] == node:
                node_Sizes.append(float(row["population_density"]) * 8)
                break
    if len(node_Sizes) < index: #SomeCountry with no density
        node_Sizes.append(300.00)

    if node in EU:
        color_Map.append('#72AFE4') #EU countries are blue
    else:
        color_Map.append('#E4A872') #None EU countries are red

pos = nx.spring_layout(g, k=0.7, iterations=45)
nx.draw(g, pos, node_size = node_Sizes, with_labels=True, node_color=color_Map, font_weight='bold', font_size=10,font_color="black", **{"alpha": 0.9})
plt.show()