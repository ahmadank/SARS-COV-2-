import networkx as nx
import matplotlib.pyplot as plt
import csv

g = nx.Graph()
EU = ["Austria", "Belgium", "Bulgaria", "Croatia",
      "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]
color_Map = []
with open('countries.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row["country_name"] in EU):
            if(row["country_border_name"] == "" or not row["country_border_name"] in EU):
                g.add_node(row["country_name"])
            elif row["country_border_name"] in EU:
                if row["country_name"] == "France":
                    g.add_edge(
                        row["country_name"], row["country_border_name"], color='r', weight=2, value=0)
                elif row["country_name"] == "Germany":
                    g.add_edge(
                        row["country_name"], row["country_border_name"], color='r', weight=2, value=1)
                elif row["country_name"] == "Finland" or  row["country_name"] == "Sweden":
                    g.add_edge(
                        row["country_name"], row["country_border_name"], color='r', weight=2, value=1)
                else:
                    g.add_edge(row["country_name"],
                               row["country_border_name"], color='black')
for node in g:
    if node == "France":
        color_Map.append('#72AFE4') #patient 0 gets flagged in red
    else:
        color_Map.append('#E4A872')


for v in g.nodes():
    if v == "France": g.nodes[v]['state'] = "0-(France)"
    elif v == "Germany": g.nodes[v]['state'] = "1-(Germany)" 
    elif v == "Finland": g.nodes[v]['state'] = "2-(Finland)" 
    else: g.nodes[v]['state']=v


pos = nx.spring_layout(g, k=0.5, iterations=56)
colors = nx.get_edge_attributes(g, 'color').values()
weights = nx.get_edge_attributes(g, 'weight').values()
node_labels = nx.get_node_attributes(g,'state')
nx.draw_networkx_labels(g, pos, labels = node_labels)
nx.draw(g, pos, node_color=color_Map,
        font_weight='bold', edge_color=colors, width=list(weights), node_size=1500)
plt.show()
