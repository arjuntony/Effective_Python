import product
from file_parse import parse_csv


class Inventory:
    def __init__(self):
        self._pdcts = []

    def __iter__(self):
        return self._pdcts.__iter__()

    def __len__(self):
        return len(self._pdcts)

    def __getitem__(self, index):
        return self._pdcts[index]

    def __contains__(self, name):
        return any([p.name == name for p in self._pdcts])

    def append(self, prod):
        if not isinstance(prod, product.Product):
            raise TypeError("Expected Product object")

        self._pdcts.append(prod)

    @classmethod
    def from_csv(cls, lines, **opts):
        invdicts = parse_csv(lines,
                             select=["name", "quant", "price"],
                             types=[str, int, float],
                             **opts)
        self = cls()
        for p in invdicts:
            self.append(product.Product(**p))
        return self

    @property
    def total_cost(self):
        return sum([p.cost for p in self._pdcts])

    def tabulate_quants(self):
        from collections import Counter
        total_units = Counter()
        for p in self._pdcts:
            total_units[p.name] += p.quant
        return total_units
