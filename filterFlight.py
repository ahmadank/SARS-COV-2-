import csv


EU = ["Austria", "Belgium", "Bulgaria", "Croatia",
      "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]

with open('flights.csv', 'rt') as input, open('flightsFiltered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["country", "day", "domestic_flights",
                    "international_departures",	"international_arrivals",	"total_flights"])
    for row in csv.reader(input):
        if row[0] in EU:
            writer.writerow(row)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Filtering the data to get EU airports and their gps code
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
EU_CODE = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU",
           "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE"]
euAirport = []
with open('euAirports.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row["iata_code"] != ''):
            if(row["iso_country"] in EU_CODE):
                if(row["gps_code"] != row["ident"]):
                    # LERJ EPLB LEMI LCGK are not tracked  since they are local only
                    print(row["gps_code"])
                else:
                    euAirport.append(row["gps_code"])

"""""""""""""""""""""xxxxxxxxxxxx"""""""""""""""""""""""


#               FILTERING 2020 JAN DATA


"""""""""""""""""""""xxxxxxxxxxxx"""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Filtering the data to get all flights from EU to the world
                    and vice versa
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
originEu = 0
toEu = 0
index = 0
with open('flight2020JAN.csv', 'rt') as input, open('WORLD_flight2020JAN_Filtered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["callsign",	"number",	"icao24",	"registration",
                    "typecode",	"origin",	"destination",	"firstseen",	"lastseen",	"day"])
    for row in csv.reader(input):
        isOrigin = row[5] in euAirport
        isDest = row[6] in euAirport
        if (row[5] != '' and row[6] != '') and (isOrigin or isDest):
            index += 1
            if(isOrigin):
                originEu += 1
            else:
                toEu += 1
            print(row[5])
            writer.writerow(row)
    writer.writerow(['Total Flights from EU', originEu,
                    'Total Flights to EU', toEu, "Total",  index])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Filtering the data to get all flights from within the EU
                           only
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
index = 0
with open('flight2020JAN.csv', 'rt') as input, open('EU_flight2020JAN_Filtered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["callsign",	"number",	"icao24",	"registration",
                    "typecode",	"origin",	"destination",	"firstseen",	"lastseen",	"day"])
    for row in csv.reader(input):
        isOrigin = row[5] in euAirport
        isDest = row[6] in euAirport
        if (row[5] != '' and row[6] != '') and (isOrigin and isDest):
            index += 1
            print(row[5])
            writer.writerow(row)
    writer.writerow(["Total",  index])


"""""""""""""""""""""xxxxxxxxxxxx"""""""""""""""""""""""


#               FILTERING 2019 DEC DATA


"""""""""""""""""""""xxxxxxxxxxxx"""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Filtering the data to get all flights from EU to the world
                    and vice versa
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
originEu = 0
toEu = 0
index = 0
with open('flight2019DEC.csv', 'rt') as input, open('WORLD_flight2019DEC_Filtered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["callsign",	"number",	"icao24",	"registration",
                    "typecode",	"origin",	"destination",	"firstseen",	"lastseen",	"day"])
    for row in csv.reader(input):
        isOrigin = row[5] in euAirport
        isDest = row[6] in euAirport
        if (row[5] != '' and row[6] != '') and (isOrigin or isDest):
            index += 1
            if(isOrigin):
                originEu += 1
            else:
                toEu += 1
            print(row[5])
            writer.writerow(row)
    writer.writerow(['Total Flights from EU', originEu,
                    'Total Flights to EU', toEu, "Total",  index])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Filtering the data to get all flights from within the EU
                           only
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
index = 0
with open('flight2019DEC.csv', 'rt') as input, open('EU_flight2019DEC_Filtered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["callsign",	"number",	"icao24",	"registration",
                    "typecode",	"origin",	"destination",	"firstseen",	"lastseen",	"day"])
    for row in csv.reader(input):
        isOrigin = row[5] in euAirport
        isDest = row[6] in euAirport
        if (row[5] != '' and row[6] != '') and (isOrigin and isDest):
            index += 1
            print(row[5])
            writer.writerow(row)
    writer.writerow(["Total",  index])

"""""""""""""""""""""xxxxxxxxxxxx"""""""""""""""""""""""


#               FILTERING 2020 FEB DATA


"""""""""""""""""""""xxxxxxxxxxxx"""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Filtering the data to get all flights from EU to the world
                    and vice versa
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
originEu = 0
toEu = 0
index = 0
with open('flight2020FEB.csv', 'rt') as input, open('WORLD_flight2020FEB_Filtered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["callsign",	"number",	"icao24",	"registration",
                    "typecode",	"origin",	"destination",	"firstseen",	"lastseen",	"day"])
    for row in csv.reader(input):
        isOrigin = row[5] in euAirport
        isDest = row[6] in euAirport
        if (row[5] != '' and row[6] != '') and (isOrigin or isDest):
            index += 1
            if(isOrigin):
                originEu += 1
            else:
                toEu += 1
            print(row[5])
            writer.writerow(row)
    writer.writerow(['Total Flights from EU', originEu,
                    'Total Flights to EU', toEu, "Total",  index])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Filtering the data to get all flights from within the EU
                           only
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
index = 0
with open('flight2020FEB.csv', 'rt') as input, open('EU_flight2020FEB_Filtered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["callsign",	"number",	"icao24",	"registration",
                    "typecode",	"origin",	"destination",	"firstseen",	"lastseen",	"day"])
    for row in csv.reader(input):
        isOrigin = row[5] in euAirport
        isDest = row[6] in euAirport
        if (row[5] != '' and row[6] != '') and (isOrigin and isDest):
            index += 1
            print(row[5])
            writer.writerow(row)
    writer.writerow(["Total",  index])


"""""""""""""""""""""xxxxxxxxxxxx"""""""""""""""""""""""


#               FILTERING 2020 APRIL DATA


"""""""""""""""""""""xxxxxxxxxxxx"""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Filtering the data to get all flights from EU to the world
                    and vice versa
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
originEu = 0
toEu = 0
index = 0
with open('flight2020APRIL.csv', 'rt') as input, open('WORLD_flight2020APRIL_Filtered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["callsign",	"number",	"icao24",	"registration",
                    "typecode",	"origin",	"destination",	"firstseen",	"lastseen",	"day"])
    for row in csv.reader(input):
        isOrigin = row[5] in euAirport
        isDest = row[6] in euAirport
        if (row[5] != '' and row[6] != '') and (isOrigin or isDest):
            index += 1
            if(isOrigin):
                originEu += 1
            else:
                toEu += 1
            print(row[5])
            writer.writerow(row)
    writer.writerow(['Total Flights from EU', originEu,
                    'Total Flights to EU', toEu, "Total",  index])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Filtering the data to get all flights from within the EU
                           only
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
index = 0
with open('flight2020APRIL.csv', 'rt') as input, open('EU_flight2020APRIL_Filtered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["callsign",	"number",	"icao24",	"registration",
                    "typecode",	"origin",	"destination",	"firstseen",	"lastseen",	"day"])
    for row in csv.reader(input):
        isOrigin = row[5] in euAirport
        isDest = row[6] in euAirport
        if (row[5] != '' and row[6] != '') and (isOrigin and isDest):
            index += 1
            print(row[5])
            writer.writerow(row)
    writer.writerow(["Total",  index])
