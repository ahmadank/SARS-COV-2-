import networkx as nx
import matplotlib.pyplot as plt
import csv
import json

g=nx.Graph()
EU = ["Austria", "Belgium", "Bulgaria", "Croatia", 
"Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands"
, "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]
color_Map = []
with open('countries.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row["country_border_name"] == ""):
            g.add_node(row["country_name"])
        else:
            g.add_edge(row["country_name"],row["country_border_name"])

for node in g:
    if node in EU:
        color_Map.append('blue')
    else:
        color_Map.append('red')
print(g.number_of_nodes())
pos = nx.spring_layout(g, k=0.6, iterations=20)
nx.draw(g, pos, with_labels=True, node_color=color_Map, font_weight='bold')
bw_centrality = nx.betweenness_centrality(g, normalized=True)
plt.show()
 