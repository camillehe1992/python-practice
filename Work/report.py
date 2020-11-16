# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
    '''Read portfolio file into a list of dict'''
    portfilio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                    'name': row[0],
                    'shares':int(row[1]),
                    'price':float(row[2])
                    }
            portfilio.append(holding)
    return portfilio

def read_prices(filename):
    '''Read prices file into a dict'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) != 0:
                prices[row[0]] = float(row[1])
    return prices

def make_report(portfolio, prices):
    report = []
    for p in portfolio:
        r = (p['name'], p['shares'], prices[p['name']], prices[p['name']] - p['price'])
        report.append(r)
    return report

def caculation(report):
    '''Caculate the current value of profolio along with gain/loss'''
    total = 0.0
    flag = ''
    for name, shares, price, change in report:
        result = round(shares * change, 2)
        total += result
    return total

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- ----------')
for name, shares, price, change in report:
    #print('%10s %10d %$>10.2f %10.2f' % r)
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:10.2f}')
print('-------------------------------------------')
total = caculation(report)
print('Total: ', total)
