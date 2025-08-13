import geopy.distance

def distance(coords_1_lat,coords_1_lon,coords_2_lat,coords_2_lon):
  
  
  
  coords_1 = (coords_1_lat,coords_1_lon)
  coords_2 = (coords_2_lat,coords_2_lon)
  
  distance=geopy.distance.distance(coords_1, coords_2).km
  my_distance=round(distance,2)

  return my_distance


#Trial
"""latitude_home=46.5245
longitude_home=-80.9844

my_distance=distance(latitude_home,longitude_home,-30.0276, 166.1150)
print(my_distance)"""
