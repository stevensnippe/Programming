import requests
import time
import tkinter

"""
* master branch password: v1q
Aan de parameter key geeft je de eigen unieke API sleutel mee.
Aan de parameter datum geeft je de datum mee geschreven als: 25-10-2015. Je kunt alleen een request doen naar de TV-films voor vandaag en morgen.
Aan de parameter sorteer geeft je mee welke films je wilt ophalen. Dit is het getal 0, 1 of 2. Waar 0 staat voor: alle films, 1 staat voor: filmtips, 2 staat voor: 'film van de dag'.
"""

key = "uqs9vygkf7zfbqokuvpekg4et6s1s9b3"
datum = time.strftime("%d-%m-%Y")
sorteer = 0
response = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey='+key+'&dag='+datum+'&sorteer='+str(sorteer))
print(response.text)
kaas