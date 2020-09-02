"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

cal = calendar.TextCalendar() #This creates a plain text calendar
sysArgs = [sys.argv[i] for i in range(len(sys.argv))]
currentYear = datetime.today().year
currentMonth = datetime.today().month

if len(sysArgs) == 1:
    print(cal.prmonth(currentYear, currentMonth)) #This prints a month's calendar as returned by month(), since the length is only 1 in the system argument it will return the variables defined above, the current year and month.
elif len(sysArgs) == 2:
    print(cal.prmonth(currentYear, int(sys.argv[1]))) #It assumes you wrote in the month and it returns the input month with the current year
elif len(sysArgs) == 3:
    print(cal.prmonth(int(sys.argv[2]), int(sys.argv[1]))) #It assumes you wrote in both arguments, so it prints the month and year of what you wrote in.
else:
    print('Please enter the current month and/or year as integers, for example, 4 2020 for April 2020')