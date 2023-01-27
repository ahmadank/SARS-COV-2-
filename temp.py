
import csv
EU_FILES = ["EU_flight2019DEC_Filtered", "EU_flight2020FEB_Filtered",
            "EU_flight2020JAN_Filtered", "EU_flight2020APRIL_Filtered"]
WORLD_FILES = ["WORLD_flight2019DEC_Filtered", "WORLD_flight2020FEB_Filtered",
               "WORLD_flight2020JAN_Filtered", "WORLD_flight2020APRIL_Filtered"]
lsAiport=[]
airportIndex = []
for i in range(27):
    airportIndex.append(0)
    lsAiport.append([])
index = 0
with open('GeneratedFlightData/airportLegend.csv', newline='') as csvfile, open ('GeneratedClustering_Betweeness/EU_flight2020APRIL_FilteredFlightClustering.csv', newline='') as file2, open('EU2020AprilCLUSTER.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["CODE","Clustering_Coefficient", "Country"])
    for row in csv.DictReader(csvfile):
        a= int(row["index"])
        airportIndex[a] = row["Country"]
        lsAiport[a].append(row["Airport_gps_code"])
    
    for row in csv.DictReader(file2):
        for index, x in enumerate(lsAiport):
            if(row["AirPort"] in x): 
                writer.writerow([row["AirPort"],row["Clustering_Coefficient"], airportIndex[index] ])

