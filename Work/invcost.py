import csv
import sys
from report import read_inventory


def inventory_cost(filename):
    """
    To Calulate the Total cost of products in Inventory file
    """
    inv = read_inventory(filename)
    total = 0.0

    for pdct in inv:
        total += pdct["quant"] * pdct["price"]

    return total


    # with open(filename) as FH:
    #     rows = csv.reader(FH)
    #     headers = next(rows)
    #     total = 0.0
    #
    #     for row_num, row in enumerate(rows, start=1):
    #         record = dict(zip(headers, row))
    #         try:
    #             quant = int(record["quant"])
    #             price = float(record["price"])
    #             total += quant*price
    #         except ValueError:
    #            # print("Row" ,row_num,":","Couldnt convert :",row )
    #             print(f"Row {row_num} : Couldnt convert : {row}")
    #
    # return total


if len(sys.argv) == 2 :
    filename = sys.argv[1]
else:
    filename = "Data/inventory.csv"

cost = inventory_cost(filename)
print("Total_Cost", cost)