
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
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CsvTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self,rowdata):
        print(','.join(rowdata))


class HtmlTableFormatter(TableFormatter):
    pass