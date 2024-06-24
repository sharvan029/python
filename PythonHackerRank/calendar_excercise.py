#02 07 1992
from datetime import datetime
import calendar
given_date = "02 07 1992"
# given_date = input("Enter Date in DD MM YYYY:")
nday = given_date[:2]
gmonth = given_date[3:5]
print(nday)
print(gmonth)

tdate =  datetime.strptime(given_date, '%d %m %Y')
weeknumber = tdate.isoweekday()
print(weeknumber)
if weeknumber <= 5:
    print("Weekday")
else:
    print("Weekend")

daylist  = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day_week = daylist[weeknumber-1]
print(day_week)
