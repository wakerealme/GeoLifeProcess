import googlemaps
from math import radians, sin, cos, sqrt

def isContainsChinese(strs):
    for c in strs:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False


def searchPlaces(gmaps, lat, lng, radius=1000, place_type='bar'):
    places = []
    search_results = gmaps.places_nearby(location=(lat, lng), radius=radius, type=place_type, language='en')
    if 'results' in search_results:
        for result in search_results['results']:
            name = result['name']
            location = result['geometry']['location']
            if(isContainsChinese(name)==False):
                places.append({'name': name, 'latitude': location['lat'], 'longitude': location['lng']})
                print(f"Name: {name}, Latitude: {location['lat']}, Longitude: {location['lng']}")
    return places


if __name__ == '__main__':
    api_key = 'YOUR_GOOGLE_API_KEY'
    gmaps = googlemaps.Client(key=api_key)
    stayPoint={"longitude": 116.29573975, "latitude": 39.98693575, "userid": "0"}
    radius = 1000
    placeType = 'school'
    #place types: https://developers.google.com/maps/documentation/places/web-service/supported_types
    placesInfo = searchPlaces(gmaps, stayPoint['latitude'], stayPoint['longitude'], 1000, placeType)
    print(len(placesInfo))
