This library will be used to extract usa location like (city, state, abbreviation and country name) from raw location string, and it will be returned in json/dict format.

# Example fremont is  city in usa, so lets findout what will be the state and abbrevation:

from locations.main import Location

x = Location.Find_Location(text="Fremont")

print(x)

# Output will be:

{'city': 'Fremont', 'state': 'California', 'code': 'CA', 'country': 'United States'}
