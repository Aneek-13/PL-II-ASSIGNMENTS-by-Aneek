import csv

def count(file):
    with open(file) as f:
        reader = csv.reader(f)
        next(reader, None)
        return sum(1 for _ in reader)
