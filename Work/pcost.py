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
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
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
