#!/home/nik/github/try/python/latitude/bin/python

# importing geopy library and Nominatim class
from geopy.geocoders import Nominatim

# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")

# entering the location name
getLoc = loc.geocode("172 hartford street natick ma")

# printing address
print(getLoc.address)

# printing latitude and longitude
print(f"Latitude = {getLoc.latitude}\n")
print(f"Longitude = {getLoc.longitude}\n")
