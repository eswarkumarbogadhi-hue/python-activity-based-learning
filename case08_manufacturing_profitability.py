# Case Study 8: Manufacturing Cost and Profitability Analysis
# Product tuple: (name, material cost/unit, labour hours/unit, machine hours/unit, selling price/unit)

LABOUR_RATE = 120.0       # Rs per hour
MACHINE_RATE = 200.0      # Rs per hour
WASTAGE_RATE = 0.05       # 5% of material cost
PROFIT_TARGET = 20.0      # % on cost
UNITS = 100

products = [
    ("Chair",  450, 1.5, 0.5, 950),
    ("Table",  900, 2.5, 1.0, 1700),
    ("Shelf",  600, 2.0, 0.8, 1100),
    ("Stool",  200, 0.8, 0.2, 480),
]

print(f"Production run: {UNITS} units each, profit target {PROFIT_TARGET}%\n")
for p in products:
    name, material, lab_hr, mac_hr, price = p
    wastage = material * WASTAGE_RATE
    labour = lab_hr * LABOUR_RATE
    machine = mac_hr * MACHINE_RATE
    unit_cost = material + wastage + labour + machine
    profit = price - unit_cost
    margin = profit / unit_cost * 100

    total_cost = unit_cost * UNITS
    total_revenue = price * UNITS
    total_profit = total_revenue - total_cost

    print(f"Product: {name}")
    print(f"  Material {material:.2f} + Wastage {wastage:.2f} + Labour {labour:.2f} + Machine {machine:.2f}")
    print(f"  Unit cost: {unit_cost:.2f}   Selling price: {price:.2f}   Profit/unit: {profit:.2f} ({margin:.1f}%)")
    print(f"  Batch cost: {total_cost:.2f}   Revenue: {total_revenue:.2f}   Profit: {total_profit:.2f}")
    if margin >= PROFIT_TARGET:
        print("  Result: TARGET MET")
    else:
        needed = unit_cost * (1 + PROFIT_TARGET / 100)
        print(f"  Result: TARGET NOT MET - minimum price needed = {needed:.2f}")
    print()
