# report.py
#
# Exercise 2.4
from fileparse import parse_csv
from pprint import pprint

def read_portfolio(filename):
    '''Read portfolio file into a list of dict'''
    return parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    '''Read prices file into a dict'''
    prices = parse_csv(filename, types=[str,float], has_headers=False)
    return dict(prices)

def make_report(portfolio):
    '''
    Make a report
    '''
    report = []
    prices = read_prices('Data/prices.csv')
    for p in portfolio:
        r = (p['name'], p['shares'], prices[p['name']], prices[p['name']] - p['price'])
        report.append(r)
    return report

portfolio = read_portfolio('Data/portfoliodate.csv')
report = make_report(portfolio)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- ----------')
for name, shares, price, change in report:
    #print('%10s %10d %$>10.2f %10.2f' % r)
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:10.2f}')

