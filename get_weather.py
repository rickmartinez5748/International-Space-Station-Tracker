import urllib.request
import json

#This python file is to obtain the weather information


def get_iss_weather(latitude, longitude):
   
   key="884db306856a765ed4d4ecd3f01a7e3b"
   
   url=f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={key}"
   print(url)
   request=urllib.request.urlopen(url)
   weather=json.loads(request.read())
   
   temp_c=weather["main"]["temp"]-273.15
   description=weather["weather"][0]["description"]
 
   return temp_c, description

#Trial
"""weather=get_iss_weather(14.5924, -158.5676)
print(f"{weather[0]}, {weather[1]}")"""


