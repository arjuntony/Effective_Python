import csv


def parse_csv(filename, select = None , types = None):
    """
    Parse a csv fike into a list of records
    :param filename: filename
    :param select : specify  List of column name
    :param type : Datatype of each column
    :return: list if dict
    """
    with open(filename) as FH:
        rows = csv.reader(FH)
        headers = next(rows)
        records = list()
        if select:
            indices = [headers.index(column) for column in select]
            headers = select
        else:
            indices = []

        for row in rows:
            if not row:
                continue

            if indices:
                row = [row[index] for index in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            record = dict(zip(headers, row))
            records.append(record)

    return records
