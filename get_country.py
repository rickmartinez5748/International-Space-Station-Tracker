import urllib.request
import json

#This program is to obtain the country under the ISS

def get_iss_country(latitude, longitude):
   
   key="bdc_85f7ea8d3edb4637af75c3a776784593"
   
   url=f"https://api-bdc.net/data/reverse-geocode?latitude={latitude}&longitude={longitude}&localityLanguage=en&key={key}"
   print(url)
   request=urllib.request.urlopen(url)
   country_info=json.loads(request.read())
   
   country_name=country_info["countryName"]
   country_code=country_info["countryCode"]
   
   #This condition covers the possibility that ISS is bove water
   if country_name=="":
       country_name="ISS is above Water"
       country_code="No information to show"
   
   return country_name, country_code


#Trial
"""country=get_iss_country(-33.568500, -19.445900)

print(f"Country name: {country[0]}, country code:{country[1]}")"""
