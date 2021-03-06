import requests # get data from API
import time     # get current date
# import tkinter  # draw interface
# import tkinter.messagebox
import codecs
import xmltodict
import uuid     # genereer unieke code (bv bb4e9665-24c2-43c4-892a-8a997958d420) - uuid.uuid4()
import csv      # CSV bestand om unieke codes in op te slaan
# import Tkinter  # Importeert Tkinter.py (GUI.)
loginPogingen = 5
aantalgebruikers = 0
global gebruiker
gebruiker = ""


# Aan de parameter key geeft je de eigen unieke API sleutel mee.
key = "uqs9vygkf7zfbqokuvpekg4et6s1s9b3"
# Aan de parameter datum geeft je de datum mee geschreven als: 25-10-2015. Je kunt alleen een request doen naar de TV-films voor vandaag en morgen.
datum = time.strftime("%d-%m-%Y")
# Aan de parameter sorteer geeft je mee welke films je wilt ophalen. Dit is het getal 0, 1 of 2. Waar 0 staat voor: alle films, 1 staat voor: filmtips, 2 staat voor: 'film van de dag'.
sorteer = 0
global response
response = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey='+key+'&dag='+datum+'&sorteer='+str(sorteer))
# print(response.text)

def schrijf_xml(reponse):
    """Schrijft de response in films.xml
    --- bron: info uit slides
    geen failsafe bij openen want w dus word aangemaakt indien niet aanwezig"""
    bestand = codecs.open('films.xml', "w", "iso-8859-1")
    bestand.write(str(response.text))
    bestand.close()


def verwerk_xml():
    """Niet zeker van het nut van deze functie, laat staan later naar kijken
    --- bron: info uit slides
    """
    bestand = open('films.xml', 'r')
    xml_string = bestand.read()
    bestand.close()
    return xmltodict.parse(xml_string)


def escapeXML(text):
    """Replace character in string [bv: &amp --> &]
    bron: http://www.stuffaboutcode.com/2012/06/python-encode-xml-escape-characters.html"""
    text = text.replace("&amp;", "&")
    text = text.replace("&quot;", "\"")
    text = text.replace("&icirc;", "i") # moet î [rare i] zijn maar geeft raar teken
    text = text.replace("&apos;", "'")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&eacute;", "e") # moet é zijn maar geeft raar teken
    text = text.replace("&Eacute;", "e") # moet é zijn maar geeft raar teken (werkt mss in Tkinter)
    return text

def deEscapeXML(text): # besloten niet te gebruik
    """Replace character in string [bv: & --> &amp]"""
    text = text.replace("&", "&amp;")
    text = text.replace("\"", "&quot;")
    text = text.replace("i", "&icirc;") # moet î [rare i] zijn maar geeft raar teken
    text = text.replace("'", "&apos;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace("e", "&eacute;") # moet é zijn maar geeft raar teken
    return text


def login(lg, pw):
    """Extract de contents van login.csv naar een dictionary en 2 tuples,
    dit is makkelijk voor het verder werken met de data - indien
    meer tijd over herschrijven naar efficientere methode"""
    try:
        r = open('login.csv', 'r')
    except FileNotFoundError:
        w = open('login.csv', 'w', newline='')
        writer = csv.writer(w, delimiter = ',')
        writer.writerow( ("Username", "Password", "Email", "Provider", "Gender") )
        writer.writerow( ("test", "test", "test@.", "ziggo", "M") )
        w.close()
        r = open('login.csv', 'r')

    userLogins = {

    }
    reader = csv.reader(r, delimiter = ',')
    colum0 = [] # user
    colum1 = [] # pw
    for row in reader:
        for colum in reader:
            colum0.append(colum[0])
            colum1.append(colum[1])
            continue
        continue
    r.close()

    for i in range(len(colum0)):
        userLogins[colum0[i]] = colum1[i]
    # print(userLogins) # print hele dictionary voor test purpose
    # accesGranted = False # variable not used
    if lg in colum0:
        if pw == userLogins[lg]:
            accesGranted = True
            global gebruiker
            gebruiker = lg
            msg = ("[DEBUG] Login succesful.")
            print(msg)
        else:
            accesGranted = False
            msg = ("[DEBUG] Login failed, invalid password.")
            print(msg)
    else:
        accesGranted = False
        msg = ("[DEBUG] Login failed, invalid username.")
        print(msg)
    return accesGranted

def preparelogin2():
    """format login2 omdat we deze later liever opnieuw aanmaken"""
    schrijf_xml(response)
    films_dict = verwerk_xml()
    global providernamen
    providernamen = print_filmnamen(films_dict)
    w = open('login2.csv', 'w', newline='')
    writer = csv.writer(w, delimiter = ',')
    writer.writerow( ("Username", "Password", "Email", "Provider", "Gender") )
    for i in providernamen['provider']:
        writer.writerow( (i, i+"pass", "test@.", i, "NA") )

    w.close()




def login2(lg, pw):
    """Extract de contents van login.csv naar een dictionary en 2 tuples,
    dit is makkelijk voor het verder werken met de data - indien
    meer tijd over herschrijven naar efficientere methode"""
    schrijf_xml(response)
    films_dict = verwerk_xml()
    global providernamen
    providernamen = print_filmnamen(films_dict)
    # print(providernamen["provider"])
    try:
        r = open('login2.csv', 'r')
    except FileNotFoundError:
        w = open('login2.csv', 'w', newline='')
        writer = csv.writer(w, delimiter = ',')
        writer.writerow( ("Username", "Password", "Email", "Provider", "Gender") )
        for i in providernamen['provider']:
            writer.writerow( (i, i+"pass", "test@.", i, "NA") )

        w.close()
        r = open('login2.csv', 'r')

    userLogins = {

    }
    reader = csv.reader(r, delimiter = ',')
    colum0 = [] # user
    colum1 = [] # pw
    for row in reader:
        for colum in reader:
            colum0.append(colum[0])
            colum1.append(colum[1])
            continue
        continue
    r.close()

    for i in range(len(colum0)):
        userLogins[colum0[i]] = colum1[i]
    # print(userLogins) # print hele dictionary voor test purpose
    # accesGranted = False # variable not used
    if lg in colum0:
        if pw == userLogins[lg]:
            accesGranted = True
            global gebruiker
            gebruiker = lg
            msg = ("[DEBUG] Login succesful.")
            print(msg)
        else:
            accesGranted = False
            msg = ("[DEBUG] Login failed, invalid password.")
            print(msg)
    else:
        accesGranted = False
        msg = ("[DEBUG] Login failed, invalid username.")
        print(msg)
    return accesGranted


def createLogin(nLg, nPw, nEmail, nProvider, nGender, write):
    """Probeert username, password, email, provider en gender naar
    login.csv te schrijven, write staat voor schrijven naar login.csv True of False
    ivm het ophalen van data zonder te schrijven. Failsafe als er login.csv niet bestaat"""
    inUse = True
    try:
        f = open('login.csv', 'a', newline = '\n')
        r = open('login.csv', 'r')
        writer = csv.writer(f, delimiter = ',')
        reader = csv.reader(r, delimiter = ',')
    except FileNotFoundError:
        w = open('login.csv', 'w', newline='')
        writer = csv.writer(w, delimiter = ',')
        writer.writerow( ("Username", "Password", "Email", "Provider", "Gender") )
        writer.writerow( ("t", "t", "test@.", "ziggo", "M") )
        w.close()
        f = open('login.csv', 'a', newline = '\n')
        r = open('login.csv', 'r')
        writer = csv.writer(f, delimiter = ',')
        reader = csv.reader(r, delimiter = ',')

    for row in reader:
        # print(row[0]) # DEBUG: print alle usernames
        if nLg == (row[0]):
            print("[DEBUG] Gebruikersnaam bestaat al.")
            inUse = True
            break
        else:
            inUse = False
            continue

    if inUse == False and write == True:
    # if row[0] != 'naam': # TODO: schrijft alleen als naam en wachtwoord er al staan of file niet bestaat
    # writer.writerow( ('naam', 'wachtwoord') )
    # writer.writerow( (nLg, nPw) )
    # else:
        writer.writerow( (nLg, nPw, nEmail, nProvider, nGender) )
    f.close()
    r.close()
    return inUse




def print_filmnamen(film_dict):
    """Zet alle titels, providers, tv_links in lists nadat deze zijn
    gefiltert van characters die we niet willen (zie escapeXML).
    Hierna word een dictionary gemaakt uit de 3 lists en deze word
    gereturnt"""
    fullString = []
    fullString1 = []
    fullString2 = []
    for film in film_dict['filmsoptv']['film']:
        s = (film['titel']) # de string
        t = (film['zender'])
        u = (film['ft_link'])
        b = escapeXML(s) # escapes(replaces) characters &amp etc and makes new string
        c = escapeXML(t)
        d = escapeXML(u)
        fullString.append(b)
        fullString1.append(c)
        fullString2.append(d)
        dictionary = {
            'titel':fullString, # titel
            'provider':fullString1, # provider
            'tv_link':fullString2 # tv_link
        }

    return dictionary # titel, provider, tv_link
        # print('{} {}'.format(film['titel'], str(film['zender'])))
        # print("Titel: "+film['titel']+" Zender:"+str(film['zender']))


def kaartjeKopen(provider, film, username, code): #code moet uit generateCode komen
    """Zet unieke code uit generateCode() in database.csv + failsafe indien
    database.csv niet bestaat."""
    try:
        f = open('database.csv', 'a', newline = '')
        writer = csv.writer(f, delimiter = ',')
    except FileNotFoundError:
        w = open('database.csv', 'w', newline='')
        w.close()
        f = open('database.csv', 'a', newline = '')
        writer = csv.writer(f, delimiter = ',')
    writer.writerow((provider, film, username, code))
    # writer.writerow((code,))
    print("[DEBUG] Unieke code code aangemaakt in database: "+code)
    f.close()

def userownedfilms(gebruiker):
    """ returnt de films die een gebruiker momenteel heeft """
    try:
        r = open('database.csv', 'r')
        reader = csv.reader(r, delimiter = ',')
    except FileNotFoundError:
        w = open('database.csv', 'w', newline='')
        w.close()
        r = open('database.csv', 'r')
        reader = csv.reader(r, delimiter = ',')
    ownedfilms = []
    for row in reader:
        for colum in reader:
            if colum[2] == gebruiker:
                ownedfilms.append(colum[1])
    return ownedfilms


def generateCode():
    """Genereert een unieke code op basis van uuid4 en returnt deze, failsafe als code bestaat"""
    # UUID4: http://stackoverflow.com/questions/1210458/how-can-i-generate-a-unique-id-in-python
    try:
        r = open('database.csv', 'r')
        reader = csv.reader(r, delimiter = ',')
    except FileNotFoundError:
        w = open('database.csv', 'w', newline='')
        w.close()
        r = open('database.csv', 'r')
        reader = csv.reader(r, delimiter = ',')
    inGebruik = [] # TODO: schrijf efficienter indien tijd over
    for row in reader:
        for colum in reader:
            inGebruik.append(colum[0])
    r.close()
    code = str(uuid.uuid4())
    if code in inGebruik:
        generateCode()
    else:
        return code


def codeInDb(code):
    """kijkt of de uuid4 in de database voorkomt
    gebeurt ook al in generate code maar dit is efficienter - laten staan voor geval dat"""
    try:
        r = open('database.csv', 'r')
        reader = csv.reader(r, delimiter = ',')

    except FileNotFoundError:
        w = open('database.csv', 'w', newline='')
        w.close()
        r = open('database.csv', 'r')
        reader = csv.reader(r, delimiter = ',')

    inDb = False

    for row in reader:
       if code == (row[3]):
           inDb = True
           break
       else:
           inDb = False
           continue
    r.close()
    if inDb == True:
        print("[DEBUG] De code komt voor in de database.")
    else:
        print("[DEBUG] De code komt niet voor in de database.")
    return inDb

def aanbiederInfo(filmnaamhier):
    """zoekt de gebruikersnamen bij de ingegeven filmnaam en return deze in een list
    + failsafe als database.csv niet bestaat"""
    try:
        r = open('database.csv', 'r')
        reader = csv.reader(r, delimiter = ',')

    except FileNotFoundError:
        w = open('database.csv', 'w', newline='')
        w.close()
        r = open('database.csv', 'r')
        reader = csv.reader(r, delimiter = ',')

    ingebruikdoor = []
    amountofusers = 0
    for row in reader:
        if filmnaamhier == (row[1]):
            ingebruikdoor.append(row[2])
            amountofusers += 1
        continue
    print("[DEBUG] - in gebruik door: "+str(ingebruikdoor))
    global aantalgebruikers
    aantalgebruikers = amountofusers
    # print(str(aantalgebruikers))
    r.close()
    return ingebruikdoor

def clearFile(file): # naam van file bv clearFile('kluis.csv')
    """Maakt de csv file leeg"""
    clear = open(file, 'w')
    clear.close()
    print("[DEBUG] De inhoud van "+str(file)+" is verwijdert.")


# EINDE DEF FUNCTIES - START UITVOER (# omdat dit gebeurt in tkinter)

# aanbiederInfo('Die goldene Gans')
# clearFile #maakt gekozen file leeg
# schrijf_xml(response)
# films_dict = verwerk_xml()
# print_filmnamen(films_dict)
# print(print_filmnamen(films_dict))

# print("\n") #witregel voor overzicht
# code = generateCode()
# uuidNaarDb(code) #kan alleen uitvoeren als variable(n) boven zijn declared

# login('steven','lol') #variablen hiervoor komen uit tkinter
# createLogin('baksteen','lol') #login maken gebeurt in tkinter
# codeInDb('96df784b-606a-4ede-8eae-e1b0cdc3169b')
