import pandas as pd


# print(df.loc[df["park_name"] == "Bethune Park"])    # Dropping rows with no coordinates

def get_public_courts():
    df = pd.read_csv("geopy_courts.csv")
    df = df.dropna()
    df["coordinates"] = list(zip(df.location_lat, df.location_long))
    # print(type(df.location_lat))
    # print(dir(df.location_lat))
    # df["location_lat"] = df.location_lat.values
    # df["location_long"] = df.location_long.values
    df = df.drop(columns=['id', 'Unnamed: 0'])
    public_courts = df.to_dict('records')
    # print(type(public_courts))
    return public_courts

# get_public_courts()
# public_courts = get_public_courts()
# for court in public_courts in range(1):
#     print(court)
