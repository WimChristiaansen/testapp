import requests

def address_to_coordinates(address):
    try :
        # requesting from Geopunt
        geo_resp = requests.get("http://loc.geopunt.be/geolocation/location?q="+address+"&c=25")
        geo_loc = geo_resp.json()['LocationResult'][0]

        # Storing value into variables
        lat = geo_loc['Location']['X_Lambert72']
        lon = geo_loc['Location']['Y_Lambert72']
        return lat,lon

    except IndexError as error :
        print(error)
        print('Wrong address')
        print('Try format : "Street number, postcode city"')
