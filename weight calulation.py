weight = int(input('Weight: '))
unit = input('(L)bs or (K)gs')
if unit.upper() == 'L':
    weight_kg = weight * 0.45
    print(f"your weight is {weight_kg} kgs")
elif unit.upper() == 'K':
    weight_lbs = weight / 0.45
    print(f"your weight is {weight_lbs}")

    