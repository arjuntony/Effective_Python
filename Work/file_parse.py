import csv


def parse_csv(filename, select = None ):
    """
    Parse a csv fike into a list of records
    :param filename: filename
    :param select : List of column name to select
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

            record = dict(zip(headers, row))
            records.append(record)

    return records
