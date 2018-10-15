import urllib.request, urllib.parse, urllib.error
import json
import math
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
city = input("Please enter a City \n")
city2 = input("Please enter a City \n")
apikey = "Your API Key"

url = api_endpoint + "?q=" + city + "&appid=" + apikey
url2 = api_endpoint + "?q=" + city2 + "&appid=" + apikey

print(url)
response = urllib.request.urlopen(url)
response2 = urllib.request.urlopen(url2)
print(response)

parseResponse = json.loads(response.read())
parseResponse2 = json.loads(response2.read())
print(parseResponse)

temperature = parseResponse['main']['temp']
temperature-=273.15
t1=round(temperature,2)
weather = parseResponse['weather'][0]['description']
temperature2 = parseResponse2['main']['temp']
temperature2-=273.15
t2=round(temperature2,2)
weather2 = parseResponse2['weather'][0]['description']

print("The temperature in ",city, " is ",t1, " degrees celsuis and ", weather, "\n")
print("The temperature in ",city2, " is ",t2, " degress celsuis and ", weather2, "\n")
if(t1>t2):
    print(city, " is Warmer than ", city2)
else:
    print(city2, " is Warmer than ", city)