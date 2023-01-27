import networkx as nx
import matplotlib.pyplot as plt
import csv

g=nx.Graph()

EU_CODE = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL" , "PL", "PT", "RO", "SK", "SI", "ES", "SE"]
with open('euAirports.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row["iata_code"] != ''):
            if(row["iso_country"] in EU_CODE): 
                g.add_edge(row["iata_code"],row["iso_country"])

for code in EU_CODE:
    g.add_edge(code, "")

nx.draw(g, with_labels=True, font_weight='bold')
plt.show()
 