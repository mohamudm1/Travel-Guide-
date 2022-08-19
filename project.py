import turtle
from functools import partial
from geopy.geocoders import Nominatim
from googlesearch import search

class TravelGuide:
    """
    class which can manipulate a driven turtle around a map and log desired locations
    """
    def __init__(self):
        """
        instantiates a turtle named James
        sets up a window with width=1100, height=650, and an image of a map
        connects keys to turtle methods to create a self-driven turtle
        begins event-loop

        """
        self.james = turtle.Turtle()
        self.james.shape("turtle")
        self.james.color("red")
        self.wn = turtle.Screen()
        self.james.penup() #sets turtle to penup so the turtle doesn't draw all over the map when it moves
        self.wn.setup(width=1100, height=650, startx=0, starty=0)
        self.wn.title("Vacation Map")
        self.wn.bgpic("image.gif")
        self.wn.onkey(self.forward, "Up") #connects the forward turtle method to the up arrow key
        self.wn.onkey(self.left, "Left") #connects the left turtle method to the left arrow key
        self.wn.onkey(self.right, "Right") #connects the right turtle method to the right arrow key
        self.wn.onkey(self.quit, "q") #connects the quit (exit window) method to the Q key
        self.wn.onkey(self.log, "l") #connects the log method to the L key
        self.listofLocs = [] #List of coordinates of the user-logged locations. Contains locations in respective to the map: x, y cords
        self.newlistofLocs = [] #New list that captures the locations that have been transferred into coordinates of longitude/latitude
        self.wn.listen() #sets the window to begin listening for events
        self.wn.mainloop() #begin event loop

    def forward(self):
        """
        moves turtle forward
        """
        self.james.forward(30)

    def left(self):
        """
        angles turtle to the left
        """
        self.james.left(45)

    def right(self):
        """
        angles turtle to the right
        """
        self.james.right(45)

    def log(self):
        """
        logs and stamps the location
        """
        self.james.stamp() #stamps the logged location on the map
        self.listofLocs.append(self.james.xcor()) #adds the x value of the logged location onto the listofLocs attribute
        self.listofLocs.append(self.james.ycor()) #adds the y value of the logged location onto the listofLocs attribute



    def quit(self):
        """
        closes the window
        sets newlistofLocs attribute to a call of the function transferCords with a parameter of the attribute of the old list
        Calls getLocation function
        """
        self.wn.bye()                        # Close down the turtle window
        self.newlistofLocs = transferCords(self.listofLocs) #Creates a new list with coordinates of longitude/latitude, rather than x,y
        getLocation(self.newlistofLocs) #Calls getLocation function with newList of longitude/latitude coordinates





def getLocation(nlist):
    """
    :param nlist: new list of longitude/latitude coordinates
    :return: none
    """
    geolocator = Nominatim(user_agent="danieldoh.inbox@gmail.com", timeout=10) #Instantiates an object of Nominatim class called geolocator
    geocode = partial(geolocator.geocode, language="en")
    j = int(input("Which location do you want to explore? Input integer (Ex: 1 for location 1:) ")) #Takes user input to see which of the logged locations he/she wants to explore
    longitude = nlist[((j * 2)-2): (j*2)-1] #Quick math to locate the indices of where that locations' longitude would be. Stores it in longitude variable
    latitude = nlist[((j * 2)-1): (j*2)-0] #Quick math to locate the indices of where that locations' latitude would be. Stores it in latitude variable
    longitude = str(longitude[0]) #Captures a string version of the 0 element of the longitude. We do this so it can be formatted with geocode
    latitude = str(latitude[0]) #Captures a string version of the 0 element of the latitude. We do this so it can be formatted with geocode
    location = geolocator.geocode(latitude + "," + longitude) #Sets the location variable equal to the output from the geocode method onto the geolocator object with latitude, longitude.
    print("\nLocation of the given Latitude and Longitude:")
    newloc = (geocode((location), language = "en")) #converts location into English format so it is legible for English readers and set it to newloc variable
    newloc = str(newloc) #set it to a string version of itself so we can utilize it in searchLocations function
    print(newloc)
    yesorno = int(input("Would you like to learn more about your location? Input 1 for tourist attractions, 2 for local cuisine, 3 for tips for travel, 4 to exit : "))
    if yesorno == 1: #conditional that gives the user the option to view additional tourist attractions
        searchLocations(newloc, 1) #if user chooses to view them, it calls the searchLocations function with parameter of the location the user logged on the map and the option number
    elif yesorno == 2:
        searchLocations(newloc, 2)
    elif yesorno == 3:
        searchLocations(newloc, 3)
    else:
        pass



def searchLocations(location, num):
    """
    :param location: user's logged location
    :return: none
    """
    if num == 1:
        query = "tourist locations in" + location #creates the search topic
    if num == 2:
        query = "places to eat in" + location  # creates the search topic
    if num == 3:
        query = "tips for travel in" + location  # creates the search topic

    for j in search(query, tld="co.in", num=10, stop=10, pause=2): #for loop to catch the first 10 results on google that show up when we look up the search topic
        print(j) #prints out the results




def transferCords(list):
    """
    :param list: list of x, y coordinates of locations relative to the map
    :return: list of longitude/latitude coordinates of locations relative to the world
    """

    newlistofLocs = [] #instantiate a new list
    for i in range(len(list)):
        if i % 2 == 0: #if we are at an even indice, that means this will be an x value (longitude), so we apply a reversed version of the longitude formula from t09
            newlistofLocs.append((list[i] / (1100/2)) * 195) #add new value to the new list
        if i % 2 == 1: #if we are at an odd indice, that means this will be an y value (latitude), so we apply a reversed version of the latitude formula from t09
            newlistofLocs.append((list[i] / (650/2)) * 120) #add new value to the new list
    return newlistofLocs



def main():
    d = TravelGuide() #instantiate an object of the TravelGuide class






main()
