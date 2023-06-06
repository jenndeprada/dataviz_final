import httpx

from entities import Cancion


BASE_URL = "https://api.spotify.com/v1/tracks/"
USER_CREDENTIAL = "i7uz8re3qvxy4gnyp1r6tb192"
PASSWORD_CREDENTIAL = "Pushing20"

#Request access token 


canciones_favoritas_ids = ["4fRzunTZ51UC0oNwoVqiKB", "51NFxnQvaosfDDutk0tams", "6n05BgVkxxz2k5ICZYa2PH"]

canciones = []

for cancion in canciones_favoritas_ids:
    r = httpx.get(BASE_URL + "{cancion}")
    request = r.text
    print(request)
    cancion = Cancion(request["id"], request["name"]) #Funciona si solo hay un artista por cancion, sino hay que dinamizarlo
    canciones.append(cancion)


print(canciones)

#request["artists"][0]["name"]