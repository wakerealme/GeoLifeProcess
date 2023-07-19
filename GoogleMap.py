import googlemaps
from math import radians, sin, cos, sqrt

def isContainsChinese(strs):
    for c in strs:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False

def searchPlaces(gmaps, lat, lng, radius=500):
    places = []
    search_results = gmaps.places_nearby(location=(lat, lng), radius=radius, language='en')
    if 'results' in search_results:
        for result in search_results['results']:
            name = result['name']
            type = result['types']
            location = result['geometry']['location']
            if(isContainsChinese(name)==False):
                places.append({'type': type[0], 'name': name,  'latitude': location['lat'], 'longitude': location['lng']})
                print(f"Type:{type}, Name: {name}, Latitude: {location['lat']}, Longitude: {location['lng']}")
    return places




if __name__ == '__main__':
    api_key = 'AIzaSyAGiiAczI3P5gKeyHiGOsZ_Mp8AcM2ZbVc'
    gmaps = googlemaps.Client(key=api_key)
    stayPoint={"longitude": 116.29573975, "latitude": 39.78693575, "userid": "0"}
    radius = 1000
    # place types: https://developers.google.com/maps/documentation/places/web-service/supported_types
    placesInfo = searchPlaces(gmaps, stayPoint['latitude'], stayPoint['longitude'])








