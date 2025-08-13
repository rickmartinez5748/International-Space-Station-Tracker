import urllib.request
import json

#this program is to get the information of the country under the ISS


def get_country_info(code):
   
   url=f"https://restcountries.com/v3.1/alpha/{code}"
   request=urllib.request.urlopen(url)
   result=json.loads(request.read())
   
  #obtaining information from JSon File
   region=result[0]["region"]
   capital=result[0]["capital"][0]
   population=result[0]["population"]
   flag=result[0]["flags"]["png"]
   
   
   return region, capital, population, flag



#country="australia"
#info=get_country_info(country)
#print(f"{info[0]},{info[1]},{info[2]},{info[3]}")