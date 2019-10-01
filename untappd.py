#!/usr/bin/env python3
import json
import csv
import argparse

p = argparse.ArgumentParser()
p.add_argument('file', help='name of the json file to extract uniques from')
a = p.parse_args()

data = json.load(open(a.file))
fne = str(a.file[:len(a.file)-5]) + '-uniques.csv'
fnej = str(a.file[:len(a.file)-5]) + '-uniques.json'

uniques = list({x['beer_url']: x for x in data}.values())
csv_header = list(data[0].keys())
dupes = len(data) - len(uniques)

print("You have " + str(len(data)) + ' total check-ins with ' +
      str(len(uniques)) + ' uniques and ' + str(dupes) + ' duplicates\n')

with open(fne, 'w') as fcsv:
    cw = csv.DictWriter(fcsv, fieldnames=csv_header)
    cw.writeheader()
    for i in range(0, len(uniques)):
        cw.writerow(uniques[i])

with open(fnej, 'w') as fjson:
    json.dump(uniques, fjson, separators=(',', ':'))

print('Created ' + fne + ' and ' + fnej +
      ' with just your unique beer check-ins')

