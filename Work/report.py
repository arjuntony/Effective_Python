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


def make_report(pdcs, prices):
    values = list()
    for p in pdcs:
        name = p["name"]
        quant = p["quant"]
        latest_price = prices[p["name"]]
        change_in_price = p["price"] - latest_price
        row = (name, quant, latest_price, change_in_price)
        values.append(row)

    return values


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

rows = make_report(inventory, latest_prices)

headers = ('Name', 'Quantity', 'Price', 'Change')
dashes = ["-"*10, ]* 4
headers_list = list()
headers_list.append(headers)

for name,quant,price,change in headers_list:
    print(f"{name:>10s} {quant:>10s} {price:>10s} {change:>10s}")

print('{:>10} {:>10} {:>10} {:>10}'.format(*dashes))

for name,quant,price,change in rows:
    #price = '\u20B9' + str(price)
    print(f"{name:>10s} {quant:>10d} \u20B9{price:>10.2f} {change:>10.2f}")

print("\n")

print("Present Cost =", '\u20B9' + str(present_cost))
Total_gain = present_cost - total_cost
print("Total Gain is = ", '\u20B9' + str(Total_gain))

