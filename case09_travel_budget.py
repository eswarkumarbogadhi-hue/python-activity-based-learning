# Case Study 9: Multi-Currency Travel Budget Analysis
# Expense tuple: (category, amount, currency)

currencies = ["USD", "EUR", "GBP", "INR"]
rates_to_inr = [83.50, 90.20, 105.40, 1.0]
CONVERSION_FEE = 0.02     # 2% on foreign currency conversions
BUDGET = 250000.0

expenses = [
    ("Flights",       1200, "USD"),
    ("Hotel",         900,  "EUR"),
    ("Food",          400,  "EUR"),
    ("Transport",     150,  "GBP"),
    ("Sightseeing",   200,  "USD"),
    ("Visa",          12000, "INR"),
    ("Shopping",      300,  "XYZ"),     # unknown currency
]

cat_names = []
cat_totals = []
grand_total = 0.0

print(f"{'Category':<13}{'Amount':>9} {'Cur':<4}{'Rate':>8}{'Fee':>9}{'INR Total':>13}")
for e in expenses:
    cat, amt, cur = e
    pos = -1
    for i in range(len(currencies)):
        if currencies[i] == cur:
            pos = i
    if pos == -1:
        print(f"{cat:<13}{amt:>9} {cur:<4} ** unknown currency, skipped **")
        continue
    inr = amt * rates_to_inr[pos]
    fee = 0.0
    if cur != "INR":
        fee = inr * CONVERSION_FEE
    total = inr + fee
    grand_total = grand_total + total
    print(f"{cat:<13}{amt:>9} {cur:<4}{rates_to_inr[pos]:>8.2f}{fee:>9.2f}{total:>13.2f}")

    # accumulate by category
    found = -1
    for k in range(len(cat_names)):
        if cat_names[k] == cat:
            found = k
    if found == -1:
        cat_names.append(cat)
        cat_totals.append(total)
    else:
        cat_totals[found] = cat_totals[found] + total

print("-" * 55)
print(f"Total planned spending : Rs.{grand_total:,.2f}")
print(f"Budget                 : Rs.{BUDGET:,.2f}")
diff = BUDGET - grand_total
if diff >= 0:
    print(f"Within budget, remaining Rs.{diff:,.2f}")
else:
    print(f"OVER BUDGET by Rs.{-diff:,.2f}")

big = 0
for i in range(len(cat_totals)):
    if cat_totals[i] > cat_totals[big]:
        big = i
share = cat_totals[big] / grand_total * 100
print(f"Largest expense category: {cat_names[big]} (Rs.{cat_totals[big]:,.2f}, {share:.1f}% of total)")
