# -*- coding: utf-8 -*-
# !/usr/bin/python

import math


class Location:
    """
    Class Location
    """

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


def distance(start, end):
    earth_radius = 6371

    diff_lat = math.radians(start.lat) - math.radians(end.lat)
    diff_lng = math.radians(start.lng) - math.radians(end.lng)

    sin_lat = math.sin(diff_lat / 2)
    sin_lng = math.sin(diff_lng / 2)

    a = (sin_lat * sin_lat) + math.cos(math.radians(start.lat)) * math.cos(math.radians(end.lat)) * (sin_lng * sin_lng)
    c = 2 * math.asin(min(1, math.sqrt(a)))
    dist = round(earth_radius * c, 2)

    return dist


# Puerta del Sol, Madrid, Spain
start_location = Location(40.416506, -3.703783)

# Plaza Redonda, Valencia, Spain
end_location = Location(39.473572, -0.376577)

print('The distance between those 2 locations is: ' + str(distance(start_location, end_location)) + ' km.')
