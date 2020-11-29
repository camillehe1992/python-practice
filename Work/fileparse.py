# fileparse.py
#
# Exercise 3.3
import csv    

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a file into a list of record
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    # Read file headers if headers exsits
    headers = next(lines).rstrip('\n').split(delimiter) if has_headers else []
    
    # Select columns if select is provided
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for line in lines:
        if line == '\n':
            continue
        row = line.strip().split(delimiter)
        # Filter the line if specific columns were selected
        if select:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {rowno} Couldn\'t convert {row}')
                    print(f'Row {rowno}: Reason {e}')
                
        if headers:
            # Make a dict
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
            
        records.append(record)

    return records    
