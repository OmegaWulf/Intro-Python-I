"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
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
"""

import calendar
import datetime

inputs = input("Type your input as: MM YYYY").split()
now = datetime.date.today()

print(inputs)

if not inputs:
    calendar = calendar.TextCalendar()
    formatted = calendar.formatmonth(now.year, now.month)
    print(formatted)
    exit()

inputNums = [int(i) for i in inputs]

if len(inputNums) == 1:
    calendar = calendar.TextCalendar()
    formatted = calendar.formatmonth(now.year, inputNums[0])
    print(formatted)

elif len(inputNums) == 2:
    calendar = calendar.TextCalendar()
    formatted = calendar.formatmonth(inputNums[1], inputNums[0])
    print(formatted)

else:
    print("Please input your calendar month and year like: 04 2019")
    exit(1)