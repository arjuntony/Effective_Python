from follow import follow
import csv
from report import read_inventory
from tableformat import print_table, create_formatter
from product import Product


def select_clumns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dict(rows , headers):
    for row in rows:
        yield dict(zip(headers, row))


def filter_names(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


def parse_product_data(lines):
    rows = csv.reader(lines)
    rows = select_clumns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float , float])
    rows = make_dict(rows , ['name', 'price', 'change'])
    return rows


def ticker(inv_file, logfile, fmt):
    inv = read_inventory(inv_file)
    rows =  parse_product_data(follow(logfile))
    rows = filter_names(rows, inv)
    formatter = create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        rowdata = [row["name"], f'{row["price"]}', f'{row["change"]}']
        formatter.row(rowdata)


if __name__ == '__main__':
    lines = follow("Data/marketlog.csv")
    rows = parse_product_data(lines)
    for row in rows:
        print(row)
