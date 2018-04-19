'''
* Determins a users Zodiac Star Sign from their birth date

~~ Key Dates for consideration ~~

Aries (March 21-April 19)
Taurus (April 20 - May 20)
Gemini (May 21 - June 20)
Cancer (June 21 - July 22)
Leo (july 23-August 22)
Virgo (August 23 - September 22)
Libra (September 23 - October 22)
Scorpio(October 23 - November 21)
Sagitarius (November 22 - December 21)
Capricorn (December 22 - January 19)
Aquarius (January 20 - February 18)
Pisces (February 19 - March 20)
'''

# Import the datetime function to access today's date 
# Also to convert strings into a date format to be modified.

import datetime
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

myBday = input("Please enter your birthday in the format dd/mm/yyyy  ")


Day, Month, Year = map(int, myBday.split('/'))
birthday = datetime.date(Year, Month, Day)


print("Your age is: " + str(calculate_age(birthday)))


zodiac = ""

if (int(Month) == 3) and (int(Day) >= 21) or (int(Month) == 4)and (int(Day) <= 19):
    zodiac = "Aries"
elif (int(Month) == 4) and (int(Day) >= 20) or (int(Month) == 5)and (int(Day) <= 20):
    zodiac = "Taurus"
elif (int(Month) == 5) and (int(Day) >= 21) or (int(Month) == 6)and (int(Day) <= 20):
    zodiac = "Gemini"
elif (int(Month) == 6) and (int(Day) >= 21) or (int(Month) == 7)and (int(Day) <= 22):
    zodiac = "Cancer"
elif (int(Month) == 7) and (int(Day) >= 23) or (int(Month) == 8)and (int(Day) <= 22):
    zodiac = "Leo"
elif (int(Month) == 8) and (int(Day) >= 23) or (int(Month) == 9)and (int(Day) <= 22):
    zodiac = "Virgo"
elif (int(Month) == 9) and (int(Day) >= 23) or (int(Month) == 10)and (int(Day) <= 22):
    zodiac = "Libra"
elif (int(Month) == 10) and (int(Day) >= 23) or (int(Month) == 11)and (int(Day) <= 21):
    zodiac = "Scorpio"
elif (int(Month) == 11) and (int(Day) >= 22) or (int(Month) == 12)and (int(Day) <= 21):
    zodiac = "Sagitarius"
elif (int(Month) == 12) and (int(Day) >= 22) or (int(Month) == 1)and (int(Day) <= 19):
    zodiac = "Capricorn"
elif (int(Month) == 1) and (int(Day) >= 20) or (int(Month) == 4)and (int(Day) <= 18):
    zodiac = "Aquarius"
elif (int(Month) == 2) and (int(Day) >= 19) or (int(Month) == 3)and (int(Day) <= 20):
    zodiac = "Pices"    

print("Your Zodiac Start Sign is: " + zodiac)

