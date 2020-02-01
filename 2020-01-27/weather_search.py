# This is the python default library for handling urls and web requests.
# It was picked because it doesn't require installing anything on most systems
# but you may want to look at requests 'python3 -m pip install requests` 
# for something that's nicer to use
from urllib import request
import math
# This library is for reading and writing JSON data.
import json

# The day before yesterday we learned how to read an api and explore the data output.
# Today we're going to use that to build something interactive.
'''
TO DO
Might make so it let's you search again if you misspelled a word
'''
def url_to_dict(url):
    # Send the get request.
    response = request.urlopen(url)
    # Read the output.
    payload = response.read()
    # load JSON data from a string into a native python object.
    return json.loads(payload)

# The site 'metaweather.com' is a free api for weather data in some major locations.

# They have a search api
found = False
while not found:
    place = input("Please enter a place to retrieve weather for:")
    # if the place variable has spaces in between, it makes it so the url_to_dict func can take it as a parameter
    where = place.replace(" ", "%20")
    print("Thanks. Looking it up now...")
    search_output = url_to_dict(f"https://www.metaweather.com/api/location/search/?query={where}")

    if len(search_output) > 1:
        print("I didn't find \"{}\" but I found these:".format(where))
        search_result = {}
        for index, item in enumerate(search_output):
            # creates a dictionary with key - index and value - name of the city
            search_result[index] = item["title"]
        for key in search_result.keys():
            # prints the index followed by the name
            print(key, search_result[key])
        choice = input("Please enter a number to select one, or enter 'r' to search again\n")
        if choice.lower() == 'r':
            continue
        for key in search_result.keys():
            if int(choice) == key or choice.lower() == search_result[key].lower():
                place = search_result[key]
                where = place.replace(" ", "%20")
                print("Thanks. Looking it up now...\n")
                search_output = url_to_dict(f"https://www.metaweather.com/api/location/search/?query={where}")
            found = True

    woeid = search_output[0]["woeid"]
    weather_there = url_to_dict(f"https://www.metaweather.com/api/location/{woeid}")
    # stores the information needed about the weather
    weather_info = weather_there["consolidated_weather"]
    print(f"The weather in the next five days in {weather_there['title']} is:\n")
    string = "| Max | Min |"
    print("Prediction", string.rjust(15))
    for day_info in weather_info:
        keys = list(day_info.keys())
        # keys[n] where n is their position in the list
        weather_state_name = day_info[keys[1]]
        max_temp = str(math.trunc(day_info[keys[7]]))
        min_temp = str(math.trunc(day_info[keys[6]]))
        print(weather_state_name, max_temp.rjust(16 - len(weather_state_name)), min_temp.rjust(5))
    found = True

