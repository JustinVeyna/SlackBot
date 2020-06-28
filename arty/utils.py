import csv

def read_tsv(file):
    with open(file, "rb") as f:
        data = csv.reader(f, dialect="excel-tab")
    return data

def write_tsv(file, data):
    with open(file, "wb") as f:
        writer = csv.writer(f, dialect="excel-tab")
        writer.writerows(a)
