#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

# PREMIERE ETAPE : on va lire le fichier et parser touts les urls pour les mettre dans une array
urls = #fait ton job

# DEUXIEME ETAPE: on va faire ce qu'on appel un fetch pour recuperer l'html de la d'un des urls du fichier
# Toute les reponse pour reussir cette étape sont sur ce site : https://medium.com/better-programming/the-only-step-by-step-guide-youll-need-to-build-a-web-scraper-with-python-e79066bd895a
response = requests.get(urls)
soup = BeautifulSoup(response.content, "html.parser")

# Maintenant le but du jeu ça va être de scrapper un maximum d'annonce et si vous êtes chaud essayer de le faire le plus vite possible
# Pour fait une annonce vous devrez recuperer le titre et le prix de l'annonce


#    Enjoy