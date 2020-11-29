# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=None):
    '''
    Parse a file into a list of record
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        
        records = []
        # Read the file headers if headers exsits
        if has_headers:
             headers = next(rows)

             # If a column selector was given, find indices of the specified columnes.
             # Also narrow the set of headers used for resulting dictionaries
             if select:
                 indices = [headers.index(colname) for colname in select]
                 headers = select
             else:
                 indices = []
        else:
            indices = []
            headers = []
            
        for row in rows:
            if not row: # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]
            if headers:
                # Make a dict
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
