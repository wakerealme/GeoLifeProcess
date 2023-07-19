import os
import numpy as np
import pandas
import json
import sys
sys.path.append('./')

def plt2csv():
    for root, dirs, files in os.walk(".\\GeoLife", topdown=False):
        for name in files:
            if 'plt' in name:
                #print(root)
                userid = int(root.split('\\')[2])
                filepath = os.path.join(root, name)
                with open(filepath) as fp:
                    fields = {
                        'id': [],
                        "latitude": [],
                        'longitude': [],
                        'altitude': [],
                        'date': [],
                        'time': []
                    }

                    lines = fp.readlines()
                    lines = lines[6:]
                    for line in lines:
                        trajSplit = line.split(',')
                        fields['id'].append(userid)
                        fields['latitude'].append(trajSplit[0])
                        fields['longitude'].append(trajSplit[1])
                        fields['altitude'].append(trajSplit[3])
                        tempdate = trajSplit[5]
                        temptime = trajSplit[6]
                        fields['date'].append(tempdate)
                        fields['time'].append(temptime[:-1])

                    df = pandas.DataFrame(fields)
                    folerPath = './CSV/%s/%s'%(userid, tempdate)
                    if not os.path.exists(folerPath):
                        os.makedirs(folerPath)
                    df.to_csv('./CSV/%s/%s/data.csv'%(userid, tempdate))
                    print('User:', userid, tempdate, ' Finished!',)

if __name__ == '__main__':
    plt2csv()

