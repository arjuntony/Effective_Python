class Inventory:
    def __init__(self, pdcts):
        self._pdcts = pdcts

    def __iter__(self):
        return self._pdcts.__iter__()

    def __len__(self):
        return len(self._pdcts)

    def __getitem__(self, index):
        return self._pdcts[index]

    def __contains__(self, name):
        return any([p.name == name for p in self._pdcts])

    @property
    def total_cost(self):
        return sum([p.cost for p in self._pdcts])

    def tabulate_quants(self):
        from collections import Counter
        total_units = Counter()
        for p in self._pdcts:
            total_units[p.name] += p.quant
        return total_units
