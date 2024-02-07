#create a class called Airport
class Airport:
    #initialize class
    def __init__(self, airportCode, city, country): #constructor with variables for airport code, city, and country

        #initialize instance variables
        self._airportCode = airportCode
        self._country = country
        self._city = city

    #this section is the string representation of the class
    def __repr__(self):
        return str(self._airportCode) + " (" + str(self._city) + ", " + str(self._country) + ")" #print airport code, city, and country, formatted so it's easier to read

    #get airport code from an Airport object
    def getCode(self):
        return self._airportCode

    #get country from an Airport object
    def getCountry(self):
        return self._country

    #get city from an Airport object
    def getCity(self):
        return self._city

    #set city for a Airport object
    def setCity(self, city):
        self._city = city

    #set country for a Airport object
    def setCountry(self, country):
        self._country = country
