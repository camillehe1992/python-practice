#!/usr/bin/env python
# report.py
#
# Exercise 2.4

from fileparse import parse_csv
from pprint import pprint

def read_portfolio(filename):
    '''
    Read portfolio file into a list of dict
    '''
    return parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    '''
    Read prices file into a dict
    '''
    prices = parse_csv(filename, types=[str,float], has_headers=False)
    return dict(prices)

def make_report_data(portfolio, prices):
    '''
    Make a report data
    '''
    report_data = []
    for p in portfolio:
        r = (p['name'], p['shares'], prices[p['name']], prices[p['name']] - p['price'])
        report_data.append(r)
    return report_data

def portfolio_report(portfile, pricefile):
    '''
    Print report
    '''
    portfolio = read_portfolio(portfile)
    prices = read_prices(pricefile)
    report = make_report_data(portfolio, prices)
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)
        
         
def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
