from Flight import * #import everything from the Flight.py file
from Airport import * #import everything from the Airport.py file

# initialize all the lists that have to be accessible file-wide
allAirports = []
allFlights = {}
flightsTempList = []
allFlightsList = []


# this function loads the data in from the two text files provided
def loadData(airportFile, flightFile):
    # create two temporary lists for ease of access
    flightObjList = []
    tempFlightObjList = []

    # create try-except-else statement to catch any thrown exception when opening files
    try:
        airportFileContent = open(airportFile, "r", encoding="utf8")
        flightFileContent = open(flightFile, "r", encoding="utf8")
    except Exception:
        return False
    else:

        # read in airports.txt and create a list of Airport objects
        # using the data provided in the .txt file
        for line in airportFileContent:
            line = line.split(",")  # set a delimiter so we can split up our data
            obj = Airport(line[0].strip(), line[2].strip(), line[1].strip())  # create an object from the data read in
            allAirports.append(obj)  # append the object to a list

        # read in flights.txt and cleanup data/extract what's required
        # add Flight objects to a list (temporarily)
        for line in flightFileContent:
            line = line.split(",")  # set a delimiter so we can split up our data

            obj2 = Flight(line[0].strip(), getAirportByCode(line[1].strip()),
                          getAirportByCode(line[2].strip()))  # create an object from the data read in

            tempFlightObjList.append(obj2)  # append the object to a list temporarily

            flightsTempList.append(line)  # debugging line

        # initializes the dictionary with a bunch of empty lists
        for line in flightsTempList:
            allFlights[line[1]] = []

        # this block goes through every key in the dictionary and then
        # goes through every Flight available in the temporary list.
        # then, it checks the code and sees if it matches the key
        # (checking to see if origins are the same.) if they match
        # we append the object to the list that corresponds to the code
        # in the dictionary
        for key in allFlights:
            for obj in tempFlightObjList:
                if obj.getOrigin().getCode() == key:
                    allFlights[key].append(obj)
                    allFlightsList.append(obj)
            flightObjList.clear()  # clears the list for a new origin point to be filled by flights

        return True  # if all of the above executes properly, return true


# this function gets the airport of the code given
def getAirportByCode(code):
    for airport in allAirports:  # go through all airports in the list of airports
        if airport.getCode() == code:  # if codes match
            return airport  # return airport
    return -1  # if codes don't match, return -1 (there isn't any airport with that code)


# this function finds all of the flights leaving or arriving in a certain city
def findAllCityFlights(city):
    originOrDestinationCityList = []  # create a list that will be filled and returned
    for flight in allFlightsList:  # go through all flights in the list of flights
        if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city:  # if either the origin or destination of the flights is the same as the user-specified city
            originOrDestinationCityList.append(flight)  # append the flight to the list
    return originOrDestinationCityList  # return the fully-filled out list when done


# this function finds all of the flights leaving or arriving in a certain country
def findAllCountryFlights(country):
    originOrDestinationCountryList = []  # create a list that will be filled and returned
    for flight in allFlightsList:  # go through all flights in the list of flights
        if flight.getOrigin().getCountry() == country or flight.getDestination().getCountry() == country:  # if either the origin or destination of the flights is the same as the user-specified country
            originOrDestinationCountryList.append(flight)  # append the flight to the list
    return originOrDestinationCountryList  # return the fully-filled out list when done

#this function checks two things:
#1) to check for direct flights between certain airports, and
#2) to check for one-stop connections that could be flown to to get to another airport
def findFlightBetween(origAirport, destAirport):
    setOfOneHopPossibilities = set([]) #create an empty set for part 2 of the function
    for flight in allFlightsList: #go through every flight in the flights list
        if flight.getOrigin().getCode() == origAirport.getCode() and flight.getDestination().getCode() == destAirport.getCode(): #if the origin and destination are the same as the specified flights, then
            return "Direct Flight: " + origAirport.getCode() + " to " + destAirport.getCode() #return the direct flight


    for flight2 in allFlightsList: #go through every flight in the flights list again
        if flight2.getOrigin().getCode() == origAirport.getCode() and flight2.getDestination().getCode() != destAirport.getCode(): #if the origin is the same as the specified flights, but destination isn't, then
            for flight3 in allFlightsList: #go through everyb flight in the flights list AGAIN
                if flight3.getOrigin() == flight2.getDestination() and flight3.getDestination().getCode() == destAirport.getCode(): #check if the second leg of the two-leg trip has "airport x" as the stopover airport
                    setOfOneHopPossibilities.add(flight3.getOrigin().getCode()) #add the flight code to the list of possible stopover airports (airport x's)

    #once all the loops are finished, simply check to see if the set has something in it. if it does, return the set. if not, return -1 as all other attempts have failed.
    if setOfOneHopPossibilities:
        return setOfOneHopPossibilities
    else:
        return -1

#this function finds whether there is a possibility of a trip being roundtrip
#for example, a plane from toronto to montreal and then another from montreal back to toronto
def findReturnFlight(firstFlight):
    for flight in allFlightsList: #go through all the flights in the list
        if firstFlight.getOrigin().getCity() == flight.getDestination().getCity() and firstFlight.getDestination().getCity() == flight.getOrigin().getCity(): #checks if the flight given's origin is the same as the flight we're going through the list for's destination and vice versa
            return flight #returns flight if true

    return -1 #returns -1 if there is no return flight available
