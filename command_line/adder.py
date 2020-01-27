import argparse
# [ ] Write a program that reads an unspecified number of integers from the command line,
# then prints out the sum of all the numbers
# the program should also have an optional argument to show the product of the numbers (in addition to the sum)


# help message should look like:
'''
usage: adder.py [-h] [-p] [numbers [numbers ...]]      

positional arguments:
  numbers        numbers to be added (or multiplied)

optional arguments:
  -h, --help     show this help message and exit
  -p, --product  show the product of the numbers (in addition to the displayed
                 sum)
'''
parser = argparse.ArgumentParser()

parser.add_argument('num',metavar='[numbers [numbers ...]]', action='store', nargs = '*', type = int, help = 'Integer range [a, b] from which the random numbers will be chosen')
parser.add_argument('-p', action ='store', type = str,  help = 'Type (-p P) after the numbers to save the file')

args = parser.parse_args()

print(sum(args.num))