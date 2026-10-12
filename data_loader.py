# this is to import the csv files

import csv

def load_data(file_path="test_data.csv"):
    records = []
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)
    return records 