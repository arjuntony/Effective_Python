from typedproperty import String, Integer, Float


class Product:
    __slots__ = ("_name", "_quant", "_price")

    name = String("name")
    quant = Integer('quant')
    price = Float('price')

    def __init__(self, name, quant, price):
        self.name = name
        self.quant = quant
        self.price = price

    # no return statement in init

    def __repr__(self):
        return (f"Product({self.name!r},{self.quant},{self.price})")

    # @property
    # def quant(self):
    #     return self._quant

    # @quant.setter
    # def quant(self, value):
    #     if not isinstance(value , int):
    #         raise TypeError("Expected an int value")
    #     self._quant = value

    @property
    def cost(self):
        return self.quant * self.price

    def sell(self, amt):
        new_amt = self.quant - amt
        self.quant = new_amt
