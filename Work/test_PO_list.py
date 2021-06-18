import csv
import report
from pprint import pprint


inventory = report.read_inventory("Data/inventory.csv")

products = [tuple(p.values()) for p in inventory]
print(products)


pr_order = dict()
for name,quant,price in products:
    if name in pr_order:
        value = pr_order[name]
        value.append( (quant, price) )
    else:
        pr_order[name] = [(quant, price)]

pprint(pr_order)


pr_order_2 = {p[0]:[] for p in products }
pprint(pr_order_2)

for name,quant,price in products:
    # value = pr_order_2[name]
    # value.append((quant, price))
    pr_order_2[name].append((quant, price))


pprint(pr_order_2)