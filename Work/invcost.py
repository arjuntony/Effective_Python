import csv


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


cost = inventory_cost("Data/inventory.csv")
print("Total_Cost", cost)
