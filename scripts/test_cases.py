
years = ['2017','2018']
counties = ['tulsa', 'mayes', 'delaware']
types =['CM','CF']


import pickle
import zlib

case_count =0
saved_cases =[]


# restore_cases = lambda compressed_case: pickle.loads(zlib.decompress(compressed_case) )

for county in counties:
  for year in years:
    for type in types:
      file_name = f'data/{county}.{year}.{type}.cases'
      pickled_cases = zlib.decompress(open(file_name, 'rb').read(), zlib.MAX_WBITS)
      new_cases =  [case for case in pickle.loads(pickled_cases)]

      new_case_count = len(new_cases)
      case_count += new_case_count
      print(f'{file_name} added {new_case_count}')
      saved_cases += new_cases

print(f'counted case: {case_count} length saved {len(saved_cases)}')

import re
import numpy as np
import pandas as pd

columns = ['Filed','County','Type', 'CaseNumber', 'Counts','Source']
case_data = lambda c: [c.filed, c.county, c.type, c.case_number, c.counts, c.source]

def print_case(c):
    print(f'{case_data(c)}')


[print_case(c) for c in saved_cases]

# all_cases = pd.DataFrame([print_case(c) for c in saved_cases], columns = columns)
