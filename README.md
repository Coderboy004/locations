This library will be used to extract usa location like (city, state, abbreviation and country name) from raw location string, and it will be returned in json/dict format.

EXAMPLE:

from locations.main import Location

# Example fremont is  city in usa

x = Location.Find_Location(text="Fremont")

print(x)

# Output will be:

{'city': 'Fremont', 'state': 'California', 'code': 'CA', 'country': 'United States'}
