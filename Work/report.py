import csv
import sys
from pprint import pprint
from file_parse import parse_csv


def read_inventory(filename):
    """
     Read inventory file into a list of dictnories with keys as
     name,quant,prices
    :param filename: filename
    :return: list of dict
    """
    return parse_csv(filename,
                     select = ["name", "quant", "price"],
                     types = [str, int, float])

    # with open(filename) as FH:
    #     rows = csv.reader(FH)
    #     headers = next(rows)
    #     inventory = list()
    #
    #     for row in rows:
    #         record = dict(zip(headers, row))
    #         product = dict()
    #         product["name"] = record["name"]
    #         product["quant"] = int(record["quant"])
    #         product["price"] = float(record["price"])
    #         inventory.append(product)
    # return inventory


def read_prices(filename):
    """
    Read csv file of prices into a dict mapping product names to prices
    :param filename: filename
    :return: dict
    """
    return dict(parse_csv(filename, types= [str, float],
              has_headers=False))
    # with open(filename) as FH:
    #     rows = csv.reader(FH)
    #     prices = dict()
    #     for row in rows:
    #         try:
    #             prices[row[0]] = float(row[1])
    #         except IndexError as e:
    #             continue
    #
    # return prices


def make_report(pdcs, prices):
    """
    Make a list of (nmae,quant,price,change) tuples given inventory list and price dict
    :param pdcs: inventory list
    :param prices: price dict
    :return: list of tuples
    """
    values = list()
    for p in pdcs:
        name = p["name"]
        quant = p["quant"]
        latest_price = prices[p["name"]]
        change_in_price = p["price"] - latest_price
        row = (name, quant, latest_price, change_in_price)
        values.append(row)

    return values


def print_report(report):
    """
    Prints a nicely formatted table from a list of (name , quant , price , change) tuples
    :param report: list of tuples for each row

    """
    headers = ('Name', 'Quantity', 'Price', 'Change')
    dashes = ["-" * 10, ] * 4
    print('{:>10} {:>10} {:>10} {:>10}'.format(*headers))
    # print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print('{:>10} {:>10} {:>10} {:>10}'.format(*dashes))
    for name, quant, price, change in report:
        price = '\u20B9' + str(price)
        print(f"{name:>10s} {quant:>10d} {price:>10s} {change:>10.2f}")


def inventory_report(inventory_filename, prices_filename):
    """
    Make a inventory report given inventory & prices data file
    """
    # Read Data Files
    inventory = read_inventory(inventory_filename)
    latest_prices = read_prices(prices_filename)

    # Create the Report Data
    rows = make_report(inventory, latest_prices)

    # Print the Report
    print_report(rows)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f"Usage : {argv[0]} invfile pricefile")

    invfile = argv[1]
    pricefile = argv[2]
    inventory_report(invfile, pricefile)


if __name__ == "__main__":
    import sys
    main(sys.argv)

