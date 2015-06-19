# Uber Coding Challenge - Food Truck Service
The web app is hosted at 
[http://foodtruck-977.appspot.com/](http://foodtruck-977.appspot.com/)

![alt text](https://raw.githubusercontent.com/sydeX/foodtruck/master/ScreenShot.png "Uber Food Truck Screenshot")

Feature Overview
----
This web application was designed to provide food trucks information found around a specified location. Results are displayed on an interactive map and a list that supports both sorted and filtered views.

- When the page is first loaded, results are shown based on the center of San Francisco. 
- Select Sort by Name/Distance will refresh the list accordingly. 
- Both map view and list view will be updated on the fly when adjusting the distance, typing Food truck name or typing food item. 
- Clicking on an item from the list will bring up the corresponding info window on the map. 
- Every time a new address is entered, results will be refreshed with updated distance based on the new center.  

Food Truck data is sourced from 
[DataSF](http://www.datasf.org/): [Food
Trucks](https://data.sfgov.org/Permitting/Mobile-Food-Facility-Permit/rqzj-sfat)

Development
====

Front-End
----
On each page refresh, or address change, the app front-end retrieves the food truck data via a JQuery request. It then creates caches for the trucks and markers associated with each truck, so that the same data can be re-used to handle user interactions without making additional trips to back end. 

######Technologies:
* Javascript/JQuery (little experience)
* html (little experience)
* css (no prior experience)
* Google Map Javascript API

######Code:
- foodtruck/js/
- foodtruck/stylesheets/
- foodtruck/index.html


Back-End:
----
The app backend provides an API that takes in an address as input, convert address to coordinates, calculate distance towards the input address for each truck, and sends back results in JSON format containing the following:

1. Status of the request (OK/Error)
2. Coordinates of the address 
3. Food truck information

On the server side, a collection of food truck objects will be created on app start, and the same collection is used on each subsequent requests. The in-memory list is quick to process and sufficient for the purpose of this project given data size is small. Depending on the requirements and data size, other possible implementations like database can also be used.


######Technologies
* Python (2yrs experience)
* Google App Engine
* Google Map Geocode API
* Socrata Open Data API

######Code:
- foodtruck/models
- foodtruck/utilities
- foodtruck/unittests


Possible Improvements:
----
- Utilize a database at back end to store food truck data
- Front-end and integration tests
- Filter on food types
- Direction to selected food truck

