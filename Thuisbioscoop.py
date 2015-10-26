import requests #get data from API
import time     #get current date
import tkinter  #draw interface
import tkinter.messagebox
import codecs
import xmltodict
import uuid     #genereer unieke code (bv bb4e9665-24c2-43c4-892a-8a997958d420) - uuid.uuid4()
import csv      #CSV bestand om unieke codes in op te slaan

# ~---> master branch password is v1q <---~
"""
Aan de parameter key geeft je de eigen unieke API sleutel mee.
Aan de parameter datum geeft je de datum mee geschreven als: 25-10-2015. Je kunt alleen een request doen naar de TV-films voor vandaag en morgen.
Aan de parameter sorteer geeft je mee welke films je wilt ophalen. Dit is het getal 0, 1 of 2. Waar 0 staat voor: alle films, 1 staat voor: filmtips, 2 staat voor: 'film van de dag'.
"""
key = "uqs9vygkf7zfbqokuvpekg4et6s1s9b3"
datum = time.strftime("%d-%m-%Y")
sorteer = 0
response = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey='+key+'&dag='+datum+'&sorteer='+str(sorteer))
#print(response.text)

def schrijf_xml(reponse):
    """Schrijft de response in films.xml"""
    bestand = codecs.open('films.xml', "w", "iso-8859-1")
    bestand.write(str(response.text))
    bestand.close()

def verwerk_xml():
    bestand = open('films.xml', 'r')
    xml_string = bestand.read()
    bestand.close()
    return xmltodict.parse(xml_string)

def print_filmnamen(film_dict):
    """Print alle films met bijhorende zender"""
    for film in film_dict['filmsoptv']['film']:
        print(film['titel']+" "+str(film['zender']))
        #print('{} {}'.format(film['titel'], str(film['zender'])))
        #print("Titel: "+film['titel']+" Zender:"+str(film['zender']))

def kaartjeKopen(code): #code moet uit generateCode komen
    """Wijs unieke code toe en zet deze in csv bestand"""
    f = open('code.csv', 'a', newline = '')
    writer = csv.writer(f, delimiter = ',')
    writer.writerow((code,)) #ticket ID toevoegen
    f.close()

def generateCode():
    """Genereert een unieke code op basis van uuid4"""
    r = open('code.csv', 'r')
    reader = csv.reader(r, delimiter = ',')
    inGebruik = []
    for row in reader:
        for colum in reader:
            inGebruik.append(colum[0])
    code = str(uuid.uuid4())
    if code in inGebruik:
        print("TEST: code was in gebruik - herhalen")
        generateCode()
    else:
        print("TEST - geschreven code: "+code)
        return code

def clearFile(file): #naam van file bv clearFile('kluis.csv')
    """Maakt de csv file leeg"""
    clear = open(file, 'w+')
    clear.close()
    print("De inhoud van "+file+" is verwijdert.")


#clearFile #maakt gekozen file leeg
schrijf_xml(response)
films_dict = verwerk_xml()
print_filmnamen(films_dict)
print("\n") #witregel voor overzicht
code = generateCode()
kaartjeKopen(code)


