
import argparse
from datetime import datetime, date, timedelta

# [ ] Write a program that reads a date from the command line as numbers (month  then day then year),
# if the date entered is in the past, a message saying "The date has passed" should be printed
# if the date is in the future the program should display the number of days remaining from today till that date,
# there should be an optional command line flag that displays the results in total number of seconds instead of days

# help message should look like:
'''
usage: day_counter.py [-h] [-s] month day year

positional arguments:
  month                Month as a number (1, 12)
  day                  Day as a number (1, 31) depending on the month
  year                 Year as a 4 digits number (2018)

optional arguments:
  -h, --help           show this help message and exit
  -s, --total_seconds  Show the time difference in total number of seconds
'''
parser = argparse.ArgumentParser()

parser.add_argument('month', action = 'store', type = int, help = 'Month as a number (1, 12)')
parser.add_argument('day', action = 'store', type = int, help = 'Day as a number (1, 31) depending on the month')
parser.add_argument('year', action = 'store', type = int, help = 'Year as a 4 digits number (2018)')
parser.add_argument('-s', action ='store', type = str,  help = 'Type (-s S) after month, day and year to show total number of seconds in this timespan.')

args = parser.parse_args()
#print(args)

date_now = datetime.today()
dt=datetime(year = args.year, month = args.month, day = args.day)

delta = dt - date_now

if delta.total_seconds() > 0:
    if args.s == "S":
        print("The total number of seconds untill your input date is", delta.total_seconds())
    else:
        print(delta.days, "days left untill your input date")
else:
    print("This date has passed")