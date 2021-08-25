import webbrowser
import numpy as np
import pandas as pd
from math import pi, cos
import exifread
import folium
from folium.plugins import HeatMap
import sys

# the listings.csv are collected from http://insideairbnb.com/get-the-data.html
# the code for coordinates is adapted from http://insideairbnb.com/get-the-data.html

def get_coordinates(photo):
    with open(photo, 'rb') as f:
        exif_dict = exifread.process_file(f)
        lon_ref = exif_dict["GPS GPSLongitudeRef"].printable
        lon = exif_dict["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
        lon = float(lon[0]) + float(lon[1]) / 60 + float(lon[2]) / float(lon[3]) / 3600
        if lon_ref != "E":
            lon = lon * (-1)
        lat_ref = exif_dict["GPS GPSLatitudeRef"].printable
        lat = exif_dict["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
        lat = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / float(lat[3]) / 3600
        if lat_ref != "N":
            lat = lat * (-1)
    return lat, lon


def distance(hotel_range):
    p = pi / 180
    lat1 = hotel_range['lat']
    lon1 = hotel_range['lon']
    lat2 = hotel_range['latitude']
    lon2 = hotel_range['longitude']
    a = 0.5 - np.cos((lat2 - lat1) * p) / 2 + np.cos(lat1 * p) * np.cos(lat2 * p) * (1 - np.cos((lon2 - lon1) * p)) / 2
    b = 12742 * np.arcsin(np.sqrt(a)) * 1000
    return b


def has_tourism(tags):
    return 'tourism' in tags


def getdata(frame):
    temp = frame[frame['tags'].apply(has_tourism)]
    temp_of_four = frame[(frame['amenity'] == 'food_court') |
                                (frame['amenity'] == 'atm') |
                                (frame['amenity'] == 'bus_station') |
                                (frame['amenity'] == 'clinic')|
                                (frame['amenity'] == 'fast_food')]
    frames = [temp, temp_of_four]
    result = pd.concat(frames)
    return result


def main(in_directory,  max_budget):
    data = pd.read_csv("data/listings.csv")
    amenity_data = pd.read_json('data/amenities-vancouver.json.gz', lines=True)
    heat = getdata(amenity_data)
    photo = in_directory
    lat, lon = get_coordinates(photo)

    earth = 6378.137
    #Using the coordinates of one point and the distance we want to get the hotel list
    #https://stackoverflow.com/questions/7477003/calculating-new-longitude-latitude-from-old-n-meters
    m = (1 / ((2 * pi / 360) * earth)) / 1000
    new_lat1 = lat + (300 * m)
    new_lat2 = lat - (300 * m)

    new_lon1 = lon + (300 * m) / cos(lat * (pi / 180))
    new_lon2 = lon - (300 * m) / cos(lat * (pi / 180))

    hotel_range = data.loc[data['longitude'] < new_lon1]
    hotel_range = hotel_range.loc[hotel_range['longitude'] > new_lon2]
    hotel_range = hotel_range.loc[hotel_range['latitude'] < new_lat1]
    hotel_range = hotel_range.loc[hotel_range['latitude'] > new_lat2]
    if(max_budget!="all"):
        hotel_range = hotel_range.loc[hotel_range['price'] <= int(max_budget)]

    hotel_range = hotel_range.reset_index(drop=True)
    hotel_range['lon'] = lon
    hotel_range['lat'] = lat
    hotel_range['distance between'] = distance(hotel_range)
    hotel_range = hotel_range.drop(['lon', 'lat'], axis=1)
    hotel_range = hotel_range.sort_values(by='distance between')
    hotel_range.to_csv('results/hotel.csv')

    #map drawing from: https://zhuanlan.zhihu.com/p/112324234
    van_map = folium.Map(location=[lat, lon], zoom_start=16)
    lat_of_me = lat
    lon_of_me = lon
    incidents = folium.map.FeatureGroup()
    latitudes = list(hotel_range.latitude)
    longitudes = list(hotel_range.longitude)
    labels = list(hotel_range.name)
    for lat, lng, label in zip(latitudes, longitudes, labels):
        folium.Marker([lat, lng], popup=label).add_to(van_map)
    van_map.add_child(incidents)
    folium.Marker(
        location=[lat_of_me, lon_of_me],
        popup="where am I",
        icon=folium.Icon(color='red', icon="cloud" ),
    ).add_to(van_map)
    heatpoints = heat[['lat', 'lon']].values.tolist()
    HeatMap(heatpoints).add_to(van_map)
    van_map.save('results/hotel_map.html')
    van_map.save('hotel_map.html')
    webbrowser.open('hotel_map.html', new=2)
    # import os
    # os.remove("hotel_map.html")

if __name__ == '__main__':
    in_directory = sys.argv[1]
    max_budget = sys.argv[2]
    main(in_directory, max_budget)
