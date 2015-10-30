import Thuisbioscoop as TB
TB.schrijf_xml(TB.response) #
TB.films_dict = TB.verwerk_xml()
global filmnamen
filmnamen = TB.print_filmnamen(TB.films_dict)
naam = "RTL8"
list = []
filmnamenlijst = []
nummer = 0
for i in filmnamen["provider"]:
    if i == naam:
        print(nummer)
        list.append(nummer)
    nummer += 1
for provider in list:
    print(filmnamen["titel"][provider])
    filmnamenlijst.append(filmnamen["titel"][provider])
print(filmnamen["provider"])

return filmnamenlijst

