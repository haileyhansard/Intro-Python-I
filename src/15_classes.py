# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in Python is an object.

# YOUR CODE HERE
class LatLon: #This is the class LatLon
    def __init__(self, lat, lon): #This is the constructor
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon): 
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def printThis(self):
        print(self.name, self.lat, self.lon)
    def __str__(self):
        return "The waypoint {self.name} it is at latitude {self.lat} and longitue {self.lon}.".format(self=self)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint): #inherits from Waypoint
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def printAnother(self):
        print(self.name, self.difficulty, self.size, self.lat, self.lon)
    def __str__(self):
        return "The geocache {self.name} has a difficulty of {self.difficulty} and {self.size}, at latitude {self.lat} and longitude {self.lon}.".format(self=self)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
waypoint.printThis()

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", "diff 1.5", "size 2", 44.052137, -121.41556)

# Print it--also make this print more nicely
#print(geocache)
geocache.printAnother()
print(geocache)
