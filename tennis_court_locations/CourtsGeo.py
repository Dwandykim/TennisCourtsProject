import pandas as pd
from geopy.geocoders import Nominatim

df = pd.read_csv("publicCourts.csv")

# print(df.loc[:,"address"])
df['location_lat'] = ""
df['location_long'] = ""
# print(df.loc[:])

def get_coordinates():
    geolocator = Nominatim(user_agent="TennisApp")
    for i in df.index:
        try:
            address = df.loc[i,"address"]
            location = geolocator.geocode(str(address))
            df.loc[i,'location_lat'] = location.latitude
            df.loc[i,'location_long'] = location.longitude
            df.loc[i,'location_address'] = location.address

        except:
            df.loc[i,'location_lat'] = ""
            df.loc[i,'location_long'] = ""
            df.loc[i,'location_address'] = ""

    df.to_csv('geopy_courts.csv')
    
get_coordinates()