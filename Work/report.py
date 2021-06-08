import csv
import sys
from pprint import pprint


def read_inventory(filename):
    with open(filename) as FH:
        rows = csv.reader(FH)
        headers = next(rows)
        inventory = list()

        for row in rows:
            product = dict()
            product["name"] = row[0]
            product["quant"] = int(row[1])
            product["price"] = float(row[2])
            inventory.append(product)
    return inventory


def read_prices(filename):
    with open(filename) as FH:
        rows = csv.reader(FH)
        prices = dict()
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError as e:
                continue

    return prices


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/inventory.csv"

inventory = read_inventory(filename)
total_cost = 0.0
for pdct in inventory:
    total_cost += pdct["quant"] * pdct["price"]

print("Initial Cost", total_cost)

latest_prices = read_prices("Data/prices.csv")
present_cost = 0.0

for pdct in inventory:
    # pr_name = pdct["name"]
    # present_cost += # quantity * Latest Price
    present_cost += pdct["quant"] * latest_prices[pdct["name"]]

print("Present Cost =", present_cost)

Total_gain = present_cost - total_cost
print("Total Gain is = ", Total_gain)