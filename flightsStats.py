import csv


currCountry = None
currMonth = None
months = ["January", "February", "March", "April"]
domestic = 0
internationalDep = 0
internationalArrival = 0
numOfDomesticFlightsPerMonth = 0
numOfDepFlightsPerMonth = 0
numOfArrFlightsPerMonth = 0
with open('flightsFiltered.csv', 'rt') as inp, open('flightsStats.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["Country", "Month", "Domestic Flights", "Domestic count",
                    "International Departure", "Departure count", "International Arrival", "Arrival count"])
    next(inp)
    for row in csv.reader(inp):
        month = (row[1])[5] + (row[1])[6]
        if(currCountry is None):
            currCountry = row[0]
            currMonth = month
        if(row[0] != currCountry or month != currMonth):
            writer.writerow([currCountry, months[int(currMonth) - 1], domestic, numOfDomesticFlightsPerMonth,
                            internationalDep, numOfDepFlightsPerMonth, internationalArrival, numOfArrFlightsPerMonth])
            currCountry = row[0]
            currMonth = month
            domestic = 0
            internationalDep = 0
            internationalArrival = 0
            numOfDomesticFlightsPerMonth = 0
            numOfDepFlightsPerMonth = 0
            numOfArrFlightsPerMonth = 0
        if((row[2]) != ''):
            domestic += (float)(row[2])
            numOfDomesticFlightsPerMonth += 1

        if((row[3]) != ''):
            internationalDep += (float)(row[3])
            numOfDepFlightsPerMonth += 1

        if((row[4]) != ''):
            internationalArrival += (float)(row[4])
            numOfArrFlightsPerMonth += 1

""""""""""""""""""""""""""""""""""""""""""

# domestic = count of flights
# internationalDep  =  count of flights
# internationalArrival = count of flights
# numOfDomesticFlightsPerMonth = num of flights
# numOfDepFlightsPerMonth =num of flights
# numOfArrFlightsPerMonth = num of flights

""""""""""""""""""""""""""""""""""""""""""
