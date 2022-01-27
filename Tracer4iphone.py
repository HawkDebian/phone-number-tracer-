import phonenumbers

import sys

sys.ps1 = '\033[01;32m '
print(sys.ps1)

print('''

████████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗  ██║
   ██║   ███████║█████╗  ██║  ██║█████╗  ██████╔╝██║███████║██╔██╗ ██║
   ██║   ██╔══██║██╔══╝  ██║  ██║██╔══╝  ██╔══██╗██║██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗██████╔╝██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                      
                                  
                                                                        
''')

from phonenumbers import geocoder

number = input("Enter Phone Number to Trace: ")

ch_nmb = phonenumbers.parse(number, "CH")
print("Region: ", geocoder.description_for_number(ch_nmb, "en"))


from phonenumbers import carrier

service_numb = phonenumbers.parse(number, "RO")

print("Carrier: ", carrier.name_for_number(service_numb, "en"))





from phonenumbers import timezone


gb_number = phonenumbers.parse(number)

print("TimeZone: ")

lol = list(timezone.time_zones_for_number(gb_number))

print(lol)


x = phonenumbers.parse(number)

print(x)

