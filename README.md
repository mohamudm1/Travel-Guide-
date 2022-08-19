# ❗CSC226 Project

**Term**: Spring 2022

️**Author(s)**: Daniel Doh and Mostaphe Mohamud

**References**: 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, and describe how you integrated the ideas or code into your program. This includes online sources, people who have helped you, and any other resources that are not solely your own contribution. Update as you go.

We utilized the following sources:
https://www.tutorialspoint.com/how-to-get-the-longitude-and-latitude-of-a-city-using-python#:~:text=Use%20the%20geolocator.,state%2C%20and%20country%20using%20address.
https://www.geeksforgeeks.org/performing-google-search-using-python-code/
T09/ T11
We integrated all these concepts. From t11, we got the idea of the user-driven turtle. From the geopy tutorial website, we found out how to integrate the geopy module into our project to find locations from our own latitude/longitude data. And from geeksforgeeks, we learned how to integrate google searches to fulfill our goal of providing an option to the user to find tourist attractions in that area they selected.


---

## Milestone 1: Setup, Planning, Design (due 8 Apr 2022)

️**Title**: What is the title of your project?
TravelTracker!
**Purpose**: In a single sentence, describe what your project will do.
We will implement a turtle that traverses through a map and marks up the places of interest in a person's vacation, keeping track of distance and the names of the places.

️**Sources**: Which assignments or code will you base your project on?
We will base our project on T09. 

<<<<<<<<< Temporary merge branch 1
 **CRC Card**:
=========
**CRC Card**:
>>>>>>>>> Temporary merge branch 2
  - Please write a CRC card for a class that your project will implement.
  - See this link for a sample CRC card and a template to
  use for your own cards (you will have to make a copy to edit): https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing
  - Tables in markdown are not easy, so we suggest saving your CRC card
  as an image and including the image(s) in the README. You can do this
  by saving an image in the repository and linking to it. See the sample CRC card below - and replace it with your own.
  


![CRC](C:\Users\mohamudm\PycharmProjects\p01-mostaphe_daniel\MD CRC.PNG)
![CRC2](C:\Users\mohamudm\PycharmProjects\p01-mostaphe_daniel\MD CRC 2.PNG)
![WorldMap](C:\Users\mohamudm\PycharmProjects\p01-mostaphe_daniel\image\image.gif)
## Milestone 2: Code (due 15 Apr 2022)

No README action items. You should have some code and a preliminary test suite pushed to your repository. 🙃

---

## Milestone 3: Virtual Check-In (due 22 Apr 2022)

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: 0 - 100%
We have about 75% of the project done and we have 25% to get next week done.

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some strategies you can employ to increase the likelihood that you'll be successful in completing this project before the deadline.
We feel we are almost done with the project and we will be able to get it in on time. We have a couple of more features we want to add over the next week but we are confident we will get it done. 

---

## Milestone 4: Final Code, Presentation, Demo (4 May 2022 for section B, 3 May 2022 for section A)

### User Instructions
In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button. 

When you hit run, a map and a turtle will be displayed to you. 
Use the arrow keys to move the turtle around to places of your liking.
When you find a location(s) that you like, hit the L key to log them into the program. Hit the Q key when you are finished logging to exit out of the map.
After finished logging, it will prompt you to a screen asking for which location you want to find out more about. 
If you only logged 1 location, press 1. If you logged multiple, press whichever number that correlates to the order of your logged location
After it tells you the exact location of your logged location, it will ask uou if you want to explore your logged location and give you a 3 options on how to explore them: tourist attractions, local cuisine, travel tips. These options are numbered 1-2-3 respectively. When you make up your mind, enter the option number, and it'll display a google search of 10 links that are related to your search. Click on one that piques your interest.

### Errors and Constraints
Every program has bugs or features that had to be scrapped for time. Use this section to create a bullet list of all known errors and deficiencies that remain in your code. Bugs found that aren't acknowledged here will be penalized.

No known errors

### Reflection
In three to four well-written paragraphs, address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?

Overall, Game of Nim and T09 were the two choices we were going to go with, because we thought they were the most engaging assignments 
we did throughout the semester. Additionally, we knew we wanted to work with something in regards to graphics, so these two were the clear options.
Game of Nim was our original choice, but many people were doing that, so we decided to expand upon T09 since it was the next best thing.

Our final product does resemble our initial design in the sense that it works with a turtle on a map, but the overall functionality could not be more different.
Our initial design was to just have a turtle traverse through the map with a moveTurtle method. We then had other methods such as newLocation and distanceCalculation
that complemented that initial design. However, the more we worked on it, the more we felt like we needed to build something better. 
The initial design just felt too boring and impractical; We couldn't even see ourselves using it even as a joke, so why spend time developing it?

That's when we decided to make changes. We scrapped all of our boring methods and completely revamped the project. We first turned the turtle into an 
interactive, driven object that could freely traverse through the map. Since we were on the topic of utilizing keys to create interaction with the window, we decided
to link the log method onto a key, so the user could freely log any locations he or she pleased. Our goal was to have this mimic a user interface in a sense, however miniscule it may be.
We then decided to branch out of the ordinary and implemented some new modules we installed from pip such as googlesearch and geopy. These features worked perfectly with our new design.

GoogleSearch was easy to work with, but geopy was such a pain. It took some serious time and effort to translate the map's x and y coordinates into a latitude and longitude format, so we could 
adapt it into geopy. Even after we got that working, we found additional difficulties in translating the output from Geopy into English since it would automatically assume the native language of the logged location.

Nonetheless, this was a very fun and worthwhile project. We learned a lot in regards to working/creating our own classes. It's one thing to see it on text and another to make them, yourself.
Knowing what we know now, we would probably implement a lot more modules to make our project more practical for use. Geopy was so tough to work with that we felt intimidated to implement any other features.
But since we are now much more acknowledged in working with other modules, there would be further room to branch out.

