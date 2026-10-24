# Case Study 4: Employee Payroll and Deduction Analysis
# Employee tuple: (id, name, basic, overtime hours, incentive)

HRA_RATE = 0.20
DA_RATE = 0.10
OT_RATE_FACTOR = 1.5       # overtime paid at 1.5x hourly rate
HOURS_PER_MONTH = 160
PF_RATE = 0.12             # on basic

employees = [
    ("E01", "Arjun",  18000, 10, 2000),
    ("E02", "Bindu",  32000, 5,  5000),
    ("E03", "Chetan", 55000, 0,  12000),
    ("E04", "Deepa",  90000, 8,  20000),
]

line = "-" * 44
for emp in employees:
    eid, name, basic, ot_hours, incentive = emp
    hra = basic * HRA_RATE
    da = basic * DA_RATE
    hourly = basic / HOURS_PER_MONTH
    overtime = ot_hours * hourly * OT_RATE_FACTOR
    gross = basic + hra + da + overtime + incentive

    # Progressive income-tax style deduction
    tax = 0.0
    if gross > 25000:
        upper = gross
        if upper > 50000:
            upper = 50000
        tax = tax + (upper - 25000) * 0.10
    if gross > 50000:
        upper = gross
        if upper > 100000:
            upper = 100000
        tax = tax + (upper - 50000) * 0.20
    if gross > 100000:
        tax = tax + (gross - 100000) * 0.30
    if gross <= 25000:
        tax = gross * 0.05          # flat 5% for lowest slab

    pf = basic * PF_RATE
    total_deductions = tax + pf
    net = gross - total_deductions

    print(line)
    print("          SALARY STATEMENT")
    print(line)
    print(f"Employee : {eid} - {name}")
    print(f"{'Basic Pay':<20}{basic:>12.2f}")
    print(f"{'HRA (20%)':<20}{hra:>12.2f}")
    print(f"{'DA (10%)':<20}{da:>12.2f}")
    print(f"{'Overtime':<20}{overtime:>12.2f}")
    print(f"{'Incentive':<20}{incentive:>12.2f}")
    print(f"{'GROSS SALARY':<20}{gross:>12.2f}")
    print(f"{'Income Tax':<20}{tax:>12.2f}")
    print(f"{'Provident Fund':<20}{pf:>12.2f}")
    print(f"{'TOTAL DEDUCTIONS':<20}{total_deductions:>12.2f}")
    print(f"{'NET SALARY':<20}{net:>12.2f}")
    print(line)
    print()
