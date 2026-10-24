# Case Study 5: Multi-Plan Telecommunications Cost Optimization
# Plan tuple: (name, price, validity days, data GB, call minutes, extra per GB, extra per minute)

plans = [
    ("Basic",    199,  28, 28,  300,  15.0, 1.0),
    ("Standard", 299,  28, 56,  1000, 12.0, 0.8),
    ("Plus",     479,  56, 84,  2000, 10.0, 0.5),
    ("Max",      749,  84, 168, 3000, 8.0,  0.4),
    ("Lite",     149,  14, 14,  200,  20.0, 1.2),
]

days_needed = 56          # days the user wants coverage for
data_used = 90            # GB total over the period
minutes_used = 1800       # minutes total over the period
budget = 700              # maximum spend

best_name = ""
best_cost = -1

print(f"Requirement: {days_needed} days, {data_used} GB, {minutes_used} min, budget Rs.{budget}\n")
for plan in plans:
    name, price, validity, data, mins, per_gb, per_min = plan

    # number of times the plan must be recharged to cover required days
    recharges = days_needed // validity
    if days_needed % validity != 0:
        recharges = recharges + 1

    base = price * recharges
    total_data = data * recharges
    total_mins = mins * recharges

    extra_data = 0
    if data_used > total_data:
        extra_data = data_used - total_data
    extra_mins = 0
    if minutes_used > total_mins:
        extra_mins = minutes_used - total_mins

    excess = extra_data * per_gb + extra_mins * per_min
    total_cost = base + excess

    print(f"{name:<9} recharges={recharges}  base={base:<5} excess={excess:<8.2f} total={total_cost:.2f}", end="")
    if total_cost > budget:
        print("  -> OVER BUDGET")
    else:
        print("  -> eligible")
        if best_cost == -1 or total_cost < best_cost:
            best_cost = total_cost
            best_name = name

print()
if best_cost == -1:
    print("No plan fits within the budget.")
else:
    print(f"Most economical eligible plan: {best_name} (Rs.{best_cost:.2f})")
