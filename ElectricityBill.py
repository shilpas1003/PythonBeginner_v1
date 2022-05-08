import math
def bill(unit):
    ans = None
    amt = 0
    # YOUR CODE GOES HERE
    if unit <= 50:
        amt = unit * 0.50
    elif unit > 50 and unit <= 150:
        amt = 25 + (unit - 50) * 0.75
    elif unit > 100 and unit <= 250:
        amt = 100 + (unit - 150) * 1.20
    else:
        amt = 220 + (unit - 250) * 1.50

    sur_charge = amt * 0.20
    ans = amt + sur_charge

    return math.floor(ans)

print(bill(118))
