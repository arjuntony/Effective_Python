with open("Data/inventory.csv") as FH:
    headers = next(FH)
    total = 0.0
    for line in FH:
        parts = line.split(',')
        quant = int(parts[1])
        price = float(parts[2])
        total += quant*price

print("Total cost", total)