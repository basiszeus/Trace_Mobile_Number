import phonenumbers as ph
from phonenumbers import timezone,geocoder, carrier
#Tell us the time of the area where the SIM is, geo  coder to check the SIM,carrier do the work related to the SIM

# The phone number must be in a string format
# lets put it in avariable as input

number = input("Please enter your number (with +213) ")

# Let's make a variable where we pass phone number details

phone = ph.parse(number)

#variable for time zone

time = timezone.time_zones_for_number(phone)

#Same for the carrier, so the name should comeout in english

car = carrier.name_for_number(phone,"en")

#Registration to describe the code we will get in english

reg = geocoder.description_for_number(phone,"en")

#Printing
print(phone)
print(time)
print(car)
print(reg)



