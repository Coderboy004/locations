import re

from src import cities

city_database = cities.city()
city_space_database = cities.city_state_countries_with_spaces()


class Location(object):
    def __init__(self):
        self.usaStates = {"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
                          "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District Of Columbia",
                          "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois",
                          "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
                          "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota",
                          "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
                          "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
                          "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
                          "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
                          "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia",
                          "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}

    def __Replace_Spaces(self, text):
        t = str(text).strip().replace("\r", "").replace("\n", "").upper()
        for s in city_space_database:
            s = s.strip().upper()
            pattern = re.compile(rf"\b{s}\b")
            searches = re.search(pattern=pattern, string=t)
            if searches:
                t = t.replace(s, s.replace(' ', '_'))
                return t

    def __Find_State(self, text):
        state = None
        isSearch = True
        search_string = self.__Replace_Spaces(text)
        if search_string is None:
            search_string = str(text).strip().replace("\r", "").replace("\n", "").upper()
        # Split text by space and iterate on usaStates codes
        for word in search_string.split(" "):
            # Iterating on usaStates code
            if isSearch:
                for code in self.usaStates:
                    # if usa states text matches to code
                    if len(word.upper().strip()) > 1:
                        if word.upper().strip() == code.strip():
                            state = code.replace("_", " ")
                            isSearch = False
                            break
        # If state is None
        if state is None:
            for state_ in self.usaStates.values():
                pattern = re.compile(rf"\b{state_.strip().upper()}\b")
                searches = re.search(pattern=pattern, string=str(search_string.replace('_', ' ')))
                if searches:
                    state = state_
                    break
        return state

    def __Find_City(self, text):
        city = None
        isSearch = True
        search_string = self.__Replace_Spaces(text)
        if search_string is None:
            search_string = str(text).strip().replace("\r", "").replace("\n", "").upper()
        for line in search_string.split(" "):
            if isSearch:
                for code in city_database:
                    if line.upper().strip() == code.upper().strip().replace(" ", "_"):
                        city = code.replace("_", " ")
                        isSearch = False
                        break
        if city is None:
            for code_ in city_database:
                pattern = re.compile(rf"\b{code_.strip().upper()}\b")
                searches = re.search(pattern=pattern, string=str(search_string))
                if searches:
                    city = code_
                    break
        return city

    # function to return key for any value
    def __get_key(self, val):
        for key, value in self.usaStates.items():
            if val == value:
                return key

    def Find_Location(self, text):
        obj = {"city": "", "state": "", "code": "", "country": ""}
        s = self.__Find_State(text)
        c = self.__Find_City(text)
        if s is not None and c is not None:
            if len(s) > 2:
                obj['state'] = s
                obj['code'] = self.__get_key(s)
                obj['city'] = c
                obj['country'] = 'United States'
            else:
                obj['state'] = self.usaStates[s]
                obj['code'] = s
                obj['city'] = c
                obj['country'] = 'United States'
            return obj
        elif s is not None and c is None:
            if len(s) > 2:
                obj['state'] = s
                obj['code'] = self.__get_key(s)
                obj['country'] = 'United States'
            else:
                obj['state'] = self.usaStates[s]
                obj['code'] = s
                obj['country'] = 'United States'
            return obj
        elif s is None and c is not None:
            obj['state'] = ''
            obj['code'] = ''
            obj['city'] = c
            isSearches = True
            if len(c) > 2:
                if isSearches:
                    with open("../data/usa", "r") as file:
                        for line in file:
                            pattern = re.compile(rf"\b{c.strip().upper()}\b")
                            searches = re.search(pattern=pattern, string=str(line.strip().upper().replace("\r", "").replace("\n", "")))
                            if searches:
                                obj['code'] = str(line.strip().upper().replace("\r", "").replace("\n", "")).split('":')[0].replace('{"', '').strip()
                                obj['state'] = self.usaStates[obj['code']]
                                isSearches = False
                                break
            obj['country'] = 'United States'
            return obj
        elif s is None and c is None:
            search_string = self.__Replace_Spaces(text)
            if search_string is None:
                search_string = str(text).strip().replace("\r", "").replace("\n", "").upper()
            countries = {"United States Of America", "United States", "US", "U.S.", "USA", "U.S.A.", "U.S", "U.S.A"}
            for county in countries:
                county = county.strip().upper().replace(" ", "_")
                pattern = re.compile(rf"\b{county}\b")
                searches = re.search(pattern=pattern, string=str(search_string))
                if searches:
                    obj['country'] = 'United States'
                    return obj
            if obj['country'] == "":
                return {"error": "invalid location"}


if __name__ == "__main__":
    loc = Location()
    x = loc.Find_Location("Fremont")
    print(x)
