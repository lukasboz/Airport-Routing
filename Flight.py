from Airport import * #import everything from the Airport.py file

#create a class called Flight
class Flight:
    #initialize class
    def __init__(self, flightNo, origin, destination): #constructor with variables for flight number, origin, and destination
        #check if the origin and destination are Airport objects
        if isinstance(origin, Airport) is True and isinstance(destination, Airport) is True:
            #declare instance variables
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            #if the origin and destination are not airport objects, raise a TypeError that prints the below statement
            raise TypeError('the origin and destination must be airport objects')

    #this section is the string representation of the class
    def __repr__(self):
        #first check if the flight given is domestic or international (to put in the string representation later)
        if self.isDomesticFlight():
            type = 'domestic' #set type as domestic if the flight is in fact domestic
        else:
            type = 'international' #set type as international  if the flight is international

        #return the full formatted string with flight number, origin, destination, and type
        return 'Flight: ' + str(self._flightNo) + " from " + str(self._origin.getCity()) + " to " + str(self._destination.getCity()) +  ' {' + type + '}'

    #equalization function
    def __eq__(self, other):
        if self.getOrigin() == other.getOrigin() and self.getDestination() == other.getDestination() and isinstance(other, Flight):
            return True
        else:
            return False

    #get flight number from a Flight object
    def getFlightNumber(self):
        return self._flightNo

    #get origin from a Flight object
    def getOrigin(self):
        return self._origin

    #get destination from a Flight object
    def getDestination(self):
        return self._destination

    #check if a flight is domestic (whether origin and destination are in the samne country)
    def isDomesticFlight(self):
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False

    #set origin for a Flight object
    def setOrigin(self, origin):
        self._origin = origin

    #set destination for a Flight object
    def setDestination(self, destination):
        self._destination = destination

