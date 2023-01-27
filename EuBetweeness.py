import networkx as nx
import matplotlib.pyplot as plt
import csv



#This code compute Betweeness and graphs is 
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
for node in g:

    if node in EU:
        color_Map.append('#72AFE4')
    else:
        color_Map.append('#E4A872')

a = nx.betweenness_centrality(g, normalized=True)
b = nx.betweenness_centrality(g, normalized=False)

with open('betweeness.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["Country", "Value(normalized)", "Value(NOT-normalized)"])
    for country in a:
        writer.writerow([country, a[country], b[country]])

for v in g.nodes():
    str = ":{:.2f}".format((a[v]))
    g.nodes[v]['state'] = v + str

node_labels = nx.get_node_attributes(g,'state')

pos = nx.spring_layout(g, k=0.3, iterations=18)
nx.draw_networkx_labels(g, pos, font_size=10, labels = node_labels, font_weight='bold')
nx.draw(g, pos, node_size = 1200, node_color=color_Map, font_color="black", **{"alpha": 0.9})
plt.show()