This library will be used to extract usa location like (city, state, abbreviation and country name) from raw location string, and it will be returned in json/dict format.

EXAMPLE:

from locations.main import Location

x = Location.Find_Location(text="San Francisco Mumbai allahabad ca us")
print(x)