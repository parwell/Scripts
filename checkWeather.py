import urllib.request
import re
import sys
import json


wwo_weather_url = "http://api.worldweatheronline.com/free/v1/weather.ashx"
wwo_apikey = "9f6bed1339b54d1304103caef54d43cb4b1e8bd2"


def retrieveIP():
    with urllib.request.urlopen("http://checkip.dyndns.org") as url:
        query = url.read()
    return str(query)


def parseIP(query):
    ipNumberPattern = "(25[0-4]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    ipRE = "{0}.{1}.{2}.{3}".format(ipNumberPattern,ipNumberPattern,ipNumberPattern,ipNumberPattern)
    ipPattern = re.compile(ipRE)
    ip = re.search(ipPattern,query)
    return ip.group()


def queryWWO(api_url,ip):
    url = api_url + "?" + "key=" + wwo_apikey + "&q=" + ip + "&includeLocation=yes" + "&format=json"
    with urllib.request.urlopen(url) as theUrl:
        query = theUrl.read()
    return query


def parseWeather(data_json):
    weather = json.loads(data_json.decode('utf-8'))
    weather_conditions = weather['data']['current_condition'][0].items()
    for item in weather_conditions:
        if isIncluded(item):
            key = cleanUp(item[0])
            value = item[1]
            print('{}: {}'.format(key, value))


def isIncluded(item):
    ignored = ['weatherDesc','windspeedMiles','observation_time',
               'winddirDegree','visibility','weatherCode','weatherIconUrl']
    if item[0] in ignored:
        return False
    return True


def cleanUp(item):
    if item == 'temp_F':
        return 'Temperature (F)'
    if item == 'temp_C':
        return 'Temperature (C)'
    if item == 'humidity':
        return 'Humidity'
    if item == 'winddir16Point':
        return 'Wind Direction'
    if item == 'pressure':
        return 'Pressure'
    if item == 'precipMM':
        return 'Precipitation (mm)'
    if item == 'cloudcover':
        return 'Cloud Cover'
    if item == 'windspeedKmph':
        return 'Wind Speed (kmph)'
    return item


def main():
    print('Looking up local weather...\n')
    try:
        try:
            myIP = parseIP(retrieveIP())
        except:
            print('Unable to connect to Internet.')
        parseWeather(queryWWO(wwo_weather_url,myIP))
    except:
        print('Unable to connect to Worldwide Weather.')
    input()
    sys.exit()

if __name__ == "__main__":
    main()
