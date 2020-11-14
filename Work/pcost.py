# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    try:
        f = open(filename, 'rt')
        rows = csv.reader(f)
        headers = next(rows)
        cost = 0.0
        for row in rows:
            cost = int(row[1]) * float(row[2]) + cost
        f.close()
        return cost
    except FileNotFoundError:
        print('the file is not exist')

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)
