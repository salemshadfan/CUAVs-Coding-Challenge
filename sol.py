import json
import csv
import math

def main():
    with open("SensorData2.json", "r") as file:
        sensordata2 = json.load(file)

    sensordata1 =[]
    with open("SensorData1.csv", "r") as file:
        csvdata = csv.DictReader(file)
        for row in csvdata:
            sensordata1.append({
                'id':int(row["id"]),
                'latitude':float(row["latitude"]),
                'longitude':float(row["longitude"])
                })
    
    accuracy = 100
    lat_threshold = accuracy / 111000 
    
    
    resultdict = {}
    
    for i in sensordata1:
        for j in sensordata2:
            
            latcalc = abs(i['latitude'] - j['latitude'])
            longcalc = abs(i['longitude']- j['longitude'])
            threshold1 = accuracy / (111000 * math.cos(math.radians(i['latitude'])))
            threshold2 = accuracy / (111000 * math.cos(math.radians(j['latitude'])))
            lon_threshold = min(threshold1, threshold2)
            if  latcalc < lat_threshold and  longcalc < lon_threshold: 
                resultdict['{0}'.format(i['id'])] = int(j['id'])
                
    with open("Output.json","w") as file:
        json.dump(resultdict, file)

main()