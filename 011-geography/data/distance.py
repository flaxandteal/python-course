from geopy.distance import vincenty
from geopy.geocoders import Nominatim

geolocator = Nominatim()
location1 = geolocator.geocode("University Road, Belfast")
location2 = geolocator.geocode("Tipperary")
coords1 = (location1.latitude, location1.longitude)
coords2 = (location2.latitude, location2.longitude)
print("It is ", vincenty(coords1, coords2).kilometers, "km to Tipperary")
