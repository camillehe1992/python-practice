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

def caculation(portfolio, prices):
    '''Caculate the current value of profolio along with gain/loss'''
    total = 0.0
    flag = ''
    for s in portfolio:
        result = round(s['shares'] * (prices[s['name']] - s['price']), 2)
        total += result
        if result >= 0:
            flag = 'gain'
        else:
            flag = 'loss'
        print(s['name'], s['shares'], s['price'], prices[s['name']], result, flag)
    return total


portfolio = read_portfolio('Data/portfolio.csv')
pprint(portfolio)

prices = read_prices('Data/prices.csv')
pprint(prices)

total = caculation(portfolio, prices)
print('Total: ', total)
