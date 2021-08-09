class Inventory:
    def __init__(self, pdcts):
        self._pdcts = pdcts

    def __iter__(self):
        return self._pdcts.__iter__()

    @property
    def total_cost(self):
        return sum([p.cost for p in self._pdcts])

    def tabulate_quants(self):
        from collections import Counter
        total_units = Counter()
        for p in self._pdcts:
            total_units[p.name] += p.quant
        return total_units
