def create_formatter(name):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CsvTableFormatter()
    elif name == 'html':
        formatter = HtmlTableFormatter()
    else:
        print("Unkown Formatter", name)
        return None

    return formatter


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
        for name, quant, price, change in rowdata:
            print(f"{name:>10s}", f"{quant:>10d}", f"{price:>10.2f}", f"{change :>10.2f}")


class CsvTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self,rowdata):
        print(','.join(rowdata))


class HtmlTableFormatter(TableFormatter):
    pass