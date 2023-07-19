import googlemaps
from math import radians, sin, cos, sqrt

def isContainsChinese(strs):
    for c in strs:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False

def isBlockType(type):
    if(type[0]=='point_of_interest' or type[0]=='locality' or type[0]=='sublocality_level_1' or len(type)<3):
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
            if(isContainsChinese(name)==False and isBlockType(type)==False):
                places.append({'type': type[0], 'name': name,  'latitude': location['lat'], 'longitude': location['lng']})
                print(f"Type:{type}, Name: {name}, Latitude: {location['lat']}, Longitude: {location['lng']}")
    return places

if __name__ == '__main__':
    api_key = 'YOUR_GOOGLE_MAP_API'
    gmaps = googlemaps.Client(key=api_key)
    stayPoint={"longitude": 116.29573975, "latitude": 39.78693575, "userid": "0"}
    radius = 1000
    # place types: https://developers.google.com/maps/documentation/places/web-service/supported_types
    placesInfo = searchPlaces(gmaps, stayPoint['latitude'], stayPoint['longitude'], radius=radius)

### Some of Example Output
#Type:['lodging', 'point_of_interest', 'establishment'], Name: 7Days Premium Beijing Luhua Road, Latitude: 39.7884571, Longitude: 116.2876062
#Type:['shopping_mall', 'point_of_interest', 'establishment'], Name: Daily-Use Department Store, Latitude: 39.786317, Longitude: 116.301439
#Type:['convenience_store', 'store', 'food', 'point_of_interest', 'establishment'], Name: Xueyuan Supermarket, Latitude: 39.7806806, Longitude: 116.293502
#Type:['home_goods_store', 'store', 'point_of_interest', 'establishment'], Name: Theft-Proof Doors, Latitude: 39.783149, Longitude: 116.287278
#Type:['shoe_store', 'store', 'point_of_interest', 'establishment'], Name: Liangnvwu, Latitude: 39.78536500000001, Longitude: 116.299194
#Type:['restaurant', 'food', 'point_of_interest', 'establishment'], Name: Yangfang Shengli Mutton In Hot Pot, Latitude: 39.779557, Longitude: 116.293965
#Type:['restaurant', 'food', 'point_of_interest', 'establishment'], Name: Old Beijing Noodle King, Latitude: 39.780734, Longitude: 116.292956###
###




