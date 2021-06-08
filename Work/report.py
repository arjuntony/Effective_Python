import csv
import sys


def read_inventory(filename):
    with open(filename) as FH:
        rows = csv.reader(FH)
        headers = next(rows)
        inventory = list()

        for row in rows:
            product = row[0], int(row[1]), float(row[2])
            inventory.append(product)
    return inventory


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/inventory.csv"

inventory = read_inventory(filename)