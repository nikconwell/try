#!/home/nik/github/try/python/latitude/bin/python

import argparse

#
# Args
#
argParser = argparse.ArgumentParser()
argParser.add_argument('--check', dest='check', help='String to check against known good')
argParser.add_argument('--debug', dest='debug', default=False, action='store_true', help='Debug mode for various things')
argParser.add_argument('address')



args = argParser.parse_args()

print(f"You entered an address off >>>{args.address}<<<")


# importing geopy library and Nominatim class
from geopy.geocoders import Nominatim

# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")

# entering the location name
getLoc = loc.geocode(args.address)

# printing address
print(getLoc.address)

# printing latitude and longitude
print(f"Latitude = {getLoc.latitude:.6f}")
print(f"Longitude = {getLoc.longitude:.6f}")
