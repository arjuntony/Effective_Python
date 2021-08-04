def create_formatter(name):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CsvTableFormatter()
    elif name == 'html':
        formatter = HtmlTableFormatter()
    else:
        raise FormatError(f"Unkown Table Format {name}")

    return formatter


def print_table(objects,columns, formatter):
    formatter.headings(columns)
    for ele in objects:
        rowdata = list()
        for col in columns:
            rowdata.append(str(getattr(ele, col)))
        formatter.row(rowdata)


class FormatError(Exception):
    pass


class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        :param headers:
        :return:
        '''

        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of data
        :param rowdata:
        :return:
        '''

        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(('-'*10 + " ") * len(headers))

    def row(self, rowdata):
        for field in rowdata:
            print(f"{field:>10s}", end=" ")
        print()


class CsvTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self,rowdata):
        print(','.join(rowdata))


class HtmlTableFormatter(TableFormatter):
    pass