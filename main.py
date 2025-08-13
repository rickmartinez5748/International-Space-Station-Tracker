from flask import Flask, render_template
from get_iss_coordinates import get_iss_coordinates
from get_weather import get_iss_weather
from get_country import get_iss_country
from get_country_info import get_country_info
from get_distance_to_my_home import distance

app=Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    
    #Obtaining latitude and longitude of the International Space Station
    get_coordinates=get_iss_coordinates()
    latitude=get_coordinates[0]
    longitude=get_coordinates[1]
    
    #Obtaining weather under ISS
    weather=get_iss_weather(latitude, longitude)

    temp_c=round(weather[0],1) 
    description=f"{weather[1]}"
    description=description.title()
    
    #obtaining the country over which ISSS is
    country=get_iss_country(latitude, longitude)
    country_name=country[0]
    country_code=country[1]
    
    #Obtaining information about the country
    
    #In here the condition covers the possibility that ISS is above water and with this condition
    #different data is sent to the template depending if the ISSS is above water or not
    if country_name=="ISS is above Water":
        region="No information to Show"
        capital="No information to Show"
        population="No information to Show"
        flag="No flag to Show"
    
    else:    
        information=get_country_info(country_code)
        region=information[0]
        capital=information[1]
        population=information[2]
        flag=information[3]
    
    #obtaining diastance from my home to the space station
    latitude_home=46.5245
    longitude_home=-80.9844
    
    my_distance=distance(latitude_home,longitude_home,latitude,longitude)
    
    

    #Sending Everything to index.html
    return render_template("index.html", latitude=latitude, longitude=longitude, temp_c=temp_c, description=description,
                           country_name=country_name, country_code=country_code, region=region, capital=capital,
                           population=population, flag=flag, my_distance=my_distance)

if __name__=='__main__':
    app.run(host='127.0.0.1', debug=True)