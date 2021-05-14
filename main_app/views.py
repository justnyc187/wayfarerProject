from django.shortcuts import render

# Create your views here.
class City:
    def __init__(self, name, bio, img):
        self.name = name
        self.bio = bio
        self.img = img

cities = [
    City("New York", "The Big Apple", "pictureUrl"),
    City("Dallas", "Everything's bigger in Texas", "pictureUrl"),
    City("San Francisco", "Golden gate bridge", "pictureUrl"),
    City("Atlanta", "Georgia peaches", "pictureUrl"),
    City("Boston", "Real New England", "pictureUrl"),
    City("Miami", "The Sunshine City", "pictureUrl"),
    City("Las Vegas", "What happens in Vegas!", "pictureUrl"),
    City("Los Angeles", "The City of Angels", "pictureUrl"),
    City("Honolulu", "Have a luau", "pictureUrl"),
    City("St. Louis", "Golden Arches", "pictureUrl"),
    City("Chicago", "The Windy City", "pictureUrl"),
    City("London", "See the Big ben Tower", "pictureUrl"),
]