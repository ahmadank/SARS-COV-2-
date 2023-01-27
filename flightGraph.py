import csv
import networkx as nx
import matplotlib.pyplot as plt
import csv

g = nx.Graph()
EU_FILES = ["EU_flight2019DEC_Filtered", "EU_flight2020FEB_Filtered",
            "EU_flight2020JAN_Filtered", "EU_flight2020APRIL_Filtered"]
WORLD_FILES = ["WORLD_flight2019DEC_Filtered", "WORLD_flight2020FEB_Filtered",
               "WORLD_flight2020JAN_Filtered", "WORLD_flight2020APRIL_Filtered"]
COLOURS = ["#8F00FF", "#120A8F", "#30D5C8", "#EEE600", "#F28500",  "#A7FC00", "#CF71AF", "#CB410B", "#8A795D", "#C2B280", "#E0115F", "#65000B", "#E30B5D",
           "#93C572", "#FFC0CB", "#E6E200", "#002147", "#FF00FF",  "#7CFC00", "#CCCCFF", "#00A86B", "#C4C3D0",  "#FCF75E", "#B2EC5D", "#DAA520", "#00FFFF", "#E7FEFF"]
EU_CODE = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU",
           "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE"]
lsAirport = []
for i in range(27):
    lsAirport.append([])

# Comment lines 20-22 out and uncomment lines 24-26 if you want to test the world files at index i
Country = EU_FILES[0]
eu=True
color_Map = []

# Country = WORLD_FILES[0]
# eu=False
# color_Map = "#72AFE4"
with open('./flightFiltered/'+Country+'.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row["origin"] and row["destination"]):
            g.add_edge(row["origin"], row["destination"])

with open('GeneratedFlightData/airportLegend.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lsAirport[int(row["index"])].append(row["Airport_gps_code"])

if(eu):
    for node in g:
        for index, x in enumerate(lsAirport):
            print(node)
            if(node in x):
                color_Map.append(COLOURS[index])
                break
            elif(index == len(lsAirport) - 1):
                color_Map.append(COLOURS[index])

pos = nx.spring_layout(g, k=0.4, iterations=80)

largest_cluster = max(nx.connected_components(g), key=len)

a = nx.clustering(g)
with open(Country + 'FlightClustering.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["AirPort", " Clustering Coefficient"])
    for airPorts in a:
        writer.writerow([airPorts, a[airPorts]])


a = nx.betweenness_centrality(g, normalized=True)
b = nx.betweenness_centrality(g, normalized=False)
with open(Country + 'FlightBetweeness.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["Country", "Value(normalized)", "Value(NOT-normalized)"])
    for airPorts in a:
        writer.writerow([airPorts, a[airPorts], b[airPorts]])

print(g.number_of_edges())
# diameter(g)

nx.draw(g, pos, node_size=1000, with_labels=True,
                 node_color=color_Map, font_color="black", **{"alpha": 0.9})

nx.draw_circular(g, node_size=1000, with_labels=True,
                 node_color=color_Map, font_color="black", **{"alpha": 0.9})
plt.show()