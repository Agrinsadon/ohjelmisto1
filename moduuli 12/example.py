import requests

hakusana = input("Anna hakusana TV-ohjelmaan: ")
pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyynto).json()
print(vastaus)
