import csv
import sys
from pprint import pprint
from inventory import Inventory
from file_parse import parse_csv
from product import Product
import tableformat


def read_inventory(filename, **opts):
    """
     Read inventory file into a list of dictnories with keys as
     name,quant,prices
    :param filename: filename
    :return: list of dict
    """
    with open(filename) as FH:
        return Inventory.from_csv(FH)
    #     invdicts = parse_csv(FH,
    #                          select=["name", "quant", "price"],
    #                          types=[str, int, float],
    #                          **opts)
    # # inv = [Product(**p) for p in invdicts]
    # inv = Inventory()
    # for p in invdicts:
    #     inv.append(Product(**p))
    # return inv


def read_prices(filename):
    """
    Read csv file of prices into a dict mapping product names to prices
    :param filename: filename
    :return: dict
    """
    with open(filename) as FH:
        return dict(parse_csv(FH, types=[str, float],
                              has_headers=False))


def make_report(pdcs, prices):
    """
    Make a list of (nmae,quant,price,change) tuples given inventory list and price dict
    :param pdcs: inventory list
    :param prices: price dict
    :return: list of tuples
    """
    values = list()
    for p in pdcs:
        name = p.name
        quant = p.quant
        latest_price = prices[p.name]
        change_in_price = p.price - latest_price
        row = (name, quant, latest_price, change_in_price)
        values.append(row)

    return values


def print_report(report, formatter):
    """
    Prints a nicely formatted table from a list of (name , quant , price , change) tuples
    :param report: list of tuples for each row

    """
    headers = ('Name', 'Quantity', 'Price', 'Change')
    formatter.headings(headers)
    for name, quant, price, change in report:
        price = '\u20B9' + f"{price:>0.2f}"
        rowdata = [name, str(quant), f"{price:s}", f"{change:>0.2f}"]
        formatter.row(rowdata)


def inventory_report(inventory_filename, prices_filename, fmt='txt'):
    """
    Make a inventory report given inventory & prices data file
    """
    # Read Data Files
    inventory = read_inventory(inventory_filename)
    latest_prices = read_prices(prices_filename)

    # Create the Report Data
    rows = make_report(inventory, latest_prices)

    # Print the Report
    try:
        formatter = tableformat.create_formatter(fmt)
    except tableformat.FormatError as e:
        print(e)
        return

    print_report(rows, formatter)


def main(argv):
    if len(argv) < 3:
        raise SystemExit(f"Usage : {argv[0]} invfile pricefile")

    invfile = argv[1]
    pricefile = argv[2]

    try:
        format = argv[3]
    except IndexError:
        format = 'txt'

    inventory_report(invfile, pricefile, format)


if __name__ == "__main__":
    import sys

    main(sys.argv)
