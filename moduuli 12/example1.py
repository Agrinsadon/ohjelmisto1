import json
import requests

hakusana = input("Anna hakusana TV-ohjelmaan: ")

pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        vastaus_json = vastaus.json()
        #print(vastaus_json)
    for a in vastaus_json:
        print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")