import Thuisbioscoop as TB
TB.schrijf_xml(TB.response)
TB.films_dict = TB.verwerk_xml()
global filmnamen
filmnamen = TB.print_filmnamen(TB.films_dict)
print(filmnamen["provider"])