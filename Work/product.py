class Product:

    def __init__(self, name, quant, price):
        self.name = name
        self.quant = quant
        self.price = price
    # no return statement in init

    def __repr__(self):
        return (f"Product({self.name!r},{self.quant},{self.price})")

    @property
    def cost(self):
        return self.quant * self.price

    def sell(self, amt):
        new_amt = self.quant - amt
        self.quant = new_amt

