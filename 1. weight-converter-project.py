Weight = input('Weight: ')
unit = input('(L)bs or (K)gs: ')

if unit.upper() == "L":
    converted = int(Weight) * 0.45
    print(f"You are {converted} Kgs")
elif unit.upper() == "K":
    converted = int(Weight)  / 0.45
    print(f" You are {converted} Pounds")

