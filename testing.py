import Thuisbioscoop as TB
TB.schrijf_xml(TB.response)
TB.films_dict = TB.verwerk_xml()
global filmnamen
filmnamen = TB.print_filmnamen(TB.films_dict)
# provider = filmnamen["provider"].index("RTL8")
# print(provider)
list = []
nummer = 0
for i in filmnamen["provider"]:
    if i == "RTL8":
        print(nummer)
        list.append(nummer)
    nummer += 1
for provider in list:
    print(filmnamen["titel"][provider])
print(filmnamen["provider"])
