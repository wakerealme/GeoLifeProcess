# Refer to https://github.com/shanxuanchen/GeoLifeDataMining/tree/master

import sys
sys.path.append('./')
import os
import json
import pandas as pd
import datetime
# coding = utf-8
from math import radians, cos, sin, asin, sqrt


def computeMeanCord(PointArray):
    length = len(PointArray)
    longitude = 0.0
    latitude = 0.0
    for i in range(length):
        longitude = longitude + PointArray[i]["longitude"]
        latitude = latitude + PointArray[i]["latitude"]
    return {"longitude": longitude / length, "latitude": latitude / length}

"""
Calculate the great circle distance between two points on the earth (specified in decimal degrees)
"""
def haversine(lon1, lat1, lon2, lat2):  
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r * 1000




def stayPointDetection(Points, distThreh, timeThreh, MaxtimeThreh, userid):
    stayPoints = []
    i = 0
    PointNumber = len(Points)
    while i < PointNumber:
        j = i + 1
        MaxLen = -1
        while j < PointNumber:
            dist = haversine(Points[j]["longitude"], Points[j]["latitude"], Points[i]["longitude"], Points[i]["latitude"])
            if dist > MaxLen:
                MaxLen = dist
            if dist > distThreh:
                sp = {}
                T = (Points[j]['T'] - Points[i]['T']).seconds
                if T > timeThreh and T < MaxtimeThreh:
                    sp["coord"] = computeMeanCord(Points[i: j + 1])
                    sp["arvT"] = Points[i]['T']
                    sp["levT"] = Points[j]['T']
                    sp["userid"] = userid
                    stayPoints.append(sp)
                    print(T,'s pass time threshold.')
                i = j
                break
            j = j + 1
        if MaxLen < distThreh:
            break
    return stayPoints



def getPointDetection(path, distThreh, timeThreh, MaxtimeThreh, userid):
    df = pd.read_csv(path)
    logList = df['longitude'].values.tolist()
    latList = df['latitude'].values.tolist()
    dateList = df['date'].values.tolist()
    timeList = df['time'].values.tolist()

    length = len(latList)
    points = []

    for i in range(length):
        try:
            CurrentTime = datetime.datetime.strptime(dateList[i] + ":" + timeList[i], '%Y/%m/%d:%H:%M:%S')
        except:
            CurrentTime = datetime.datetime.strptime(dateList[i] + ":" + timeList[i], '%Y-%m-%d:%H:%M:%S')
        points.append({'longitude': logList[i], 'latitude': latList[i], 'T': CurrentTime, 'userid': userid})
    stayPoints = stayPointDetection(points, distThreh, timeThreh, MaxtimeThreh, userid)
    return stayPoints



if __name__ == '__main__':
    distThreh = 30
    timeThreh = 60
    MaxtimeThreh = 1000
    stayPoints = []
    for root, dirs, files in os.walk(".\\CSV\\", topdown=False):
        for name in files:
            if 'csv' in name:
                userid = root.split('\\')[-2]
                filepath = os.path.join(root, name)
                Sp = getPointDetection(filepath, distThreh, timeThreh, MaxtimeThreh, userid)
                stayPoints = stayPoints + Sp
    jsonData = []
    for point in stayPoints:
        jsonData.append({'longitude': point['coord']['longitude'], 'latitude': point['coord']['latitude'], 'userid': point["userid"]})

    folerPath = './Output/'
    if not os.path.exists(folerPath):
        os.makedirs(folerPath)

    with open("./Output/StayPoints.json", mode="w") as fp:
        json.dump(jsonData, fp)

    print(len(stayPoints))











