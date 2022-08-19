# Assignment: T09: Oh, the Places You'll Go!
#
# Purpose:  To create a map of locations
#           where the user is originally from or has visited,
#           and to use tuples and lists correctly.
######################################################################
# Acknowledgements:
#
# Original Authors: Dr. Scott Heggen and Dr. Jan Pearce

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle


def parse_file(filename):
    """
    Iterates through the file, and creates the list of places

    :param filename: the name of the file to be opened
    :return: a list representing multiple places
    """

    #####################################################
    # You do not need to modify this function!
    #####################################################

    file_content = open(filename, 'r')           # Opens file for reading

    str_num = file_content.readline()           # The first line of the file, which is the number of entries in the file
    str_num = int(str_num[:-1])                 # The '/n' character needs to be removed

    places_list = []
    for i in range(str_num):
        places_list.append(extract_place(file_content))         # Assembles the list of places

    file_content.close()

    return places_list


def place_pin(window, place):
    """
    This function places a pin on the world map.

    :param window: the window object where the pin will be placed
    :param place: a tuple object describing a place to be put on the map
    :return: None
    """

    #####################################################
    # You do not need to modify this function!
    #####################################################

    pin = turtle.Turtle()
    pin.penup()
    if len(place) == 5:
        pin.color(place[4])                     # Set the pin to user's chosen color
    pin.shape("circle")                     # Sets the pin to a circle shape

    # Logically, the denominator for longitude should be 360; lat should be 180.
    # These values (195 and 120) were determined through testing to account for
    # the extra white space on the edges of the map. You shouldn't change them!
    if len(place) == 5:
        pin.goto((place[3] / 195) * window.window_width() / 2, (place[2] / 120) * window.window_height() / 2)
    pin.stamp()                             # Stamps on the location

    text = "Unknown place"
    if len(place) == 5:
        text = "{0}'s place:\n    {1}".format(place[0], place[1])   # Setting up pin label
    pin.write(text, font=("Arial", 10, "bold"))                 # Stamps the text describing the location


def extract_place(file_content):
    """
    This function extracts five lines out of file_content,
    which is a variable holding all of the file content from the calling function. Each extracted line represents,
    in order, the place's name, location, latitude, longitude, and user color. The function returns the five elements
    to the function call as a tuple.

    :param file_content: contents of the file which represents all places
    :return: a tuple representing a single place.
    """

    name = file_content.readline().strip()
    location = file_content.readline().strip()
    latitude = file_content.readline().strip()
    longitude = file_content.readline().strip()
    user_color = file_content.readline().strip()

    # Example: place_tuple = ("Scott's example", "Somewhere special", 41, -10, "black")
    place_tuple = (name, location, float(latitude), float(longitude), user_color)
    return place_tuple


def main():
    """
    This program is designed to place pins on a world map.
    Each place is represented as a tuple.
    Each tuple is then added to a list.
    The list of tuples is used to populate the map.

    :return: None
    """

    # The next three lines set up the world map

    # A sample file was created for you to use here: places.txt
    in_file = input("Enter the name of the file: ")

    wn = turtle.Screen()
    wn.setup(width=1100, height=650, startx=0, starty=0)
    wn.bgpic("image.gif")
    wn.title("Oh, the Places You'll Go!")

    place_list = parse_file(in_file)        # generates place_list from the file

    # Iterates through each item in the place_list list, calling the place_pin() function
    for place in place_list:
        place_pin(wn, place)  # Adds ONE place to the map for each loop iteration

    print("Map created!")
    wn.exitonclick()


if __name__ == "__main__":
    main()