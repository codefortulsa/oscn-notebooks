# script for downloading Cases
import pickle
import zlib

import oscn

years = ['2017', '2018']
counties = ['mayes', 'delaware', 'tulsa']
types = ['CM', 'CF']

for county in counties:
    for year in years:
        for type in types:
            cases = oscn.request.CaseList(type=type, year=year, county=county)
            all_cases = [c for c in cases]
            file_name = f'./data/{county}.{year}.{type}.cases'
            f = open(file_name, 'wb')
            compressed_cases = zlib.compress(pickle.dumps(all_cases), 6)
            f.write(compressed_cases)
            f.close()
            print(f'{file_name}: {len(all_cases)}')
