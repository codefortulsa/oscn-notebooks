# script for downloading Cases
import pickle

import oscn

years = ['2017']
counties = ['tulsa']
types =['CM','CF']



for county in counties:
  for year in years:
    for type in types:
      cases=oscn.request.CaseList(type=type, year=year, county=county)
      # all_cases= ['howdy']
      all_cases = [c for c in cases]
      file_name = f'./data/{county}.{year}.{type}.oscn'
      f = open(file_name, 'wb')
      pickle.dump(all_cases, f)
      f.close()
      print(f'{file_name}: {len(all_cases)}')
