import csv
import sys


def inventory_cost(filename):
    with open(filename) as FH:
        rows = csv.reader(FH)
        headers = next(rows)
        total = 0.0

        for row in rows:
            quant = int(row[1])
            price = float(row[2])
            total += quant*price

    return total


if len(sys.argv) == 2 :
    filename = sys.argv[1]
else:
    filename = "Data/inventory.csv"

cost = inventory_cost(filename)
print("Total_Cost", cost)