import csv


def parse_csv(filename):
    """
    Parse a csv fike into a list of records
    :param filename: filename
    :return: list if dict
    """
    with open(filename) as FH:
        rows = csv.reader(FH)
        headers = next(rows)
        records = list()
        for row in rows:
            if not row:
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
