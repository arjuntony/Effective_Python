import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(lines, select = None , types = None, has_headers = True, delimiter = ',', silence_errors = False):
    """
    Parse a csv fike into a list of records
    :param filename: filename
    :param select : specify  List of column name
    :param type : Datatype of each column
    :param has_headers : True for Files with Headers
    :param delimiter: specify delimiter for values
    :param silence_errors : Set to True to silence erros
    :return: list if dict
    """
    if isinstance(lines, str):
        raise RuntimeError("Any iterable except the String")

    if select and not has_headers:
        raise RuntimeError("Select Requires Column Numbers")

    # with open(filename) as FH:
    rows = csv.reader(lines, delimiter = delimiter)
    # Read the file headers if presents
    if has_headers:
        headers = next(rows)
    else:
        headers = []

    # If specific column have been selected , make indices for filtering
    if select:
        indices = [headers.index(column) for column in select]
        headers = select
    else:
        indices = []

    records = list()
    for line,row in enumerate(rows, start = 1):
        if not row:
            continue

        # If specific column indices are selected , pick them out
        if indices:
            row = [row[index] for index in indices]

        # apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    # print(f"Row {line}: Coulnt convert {row} ")
                    # print(f"Row {line} : Reason {e}")
                    log.warning("Row %d: Coudlnt convert : %s", line, row)
                    log.debug("Row %d: Reason :%s", line, e)
                continue
        # make dict on a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records
