# Case Study 2: Progressive Electricity Billing

SLAB1_LIMIT = 100   # first 100 units  @ 3.50
SLAB2_LIMIT = 200   # next 100 units   @ 4.50
SLAB3_LIMIT = 300   # next 100 units   @ 6.00
RATE1, RATE2, RATE3, RATE4 = 3.50, 4.50, 6.00, 7.50   # above 300 @ 7.50
FIXED_CHARGE = 50.0
SURCHARGE_RATE = 0.05     # 5% on energy charge if units > 300
REBATE_RATE = 0.05        # 5% rebate on energy charge if units <= 100
UNUSUAL_INCREASE = 30.0   # % rise over previous month considered unusual

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
units_list = [90, 120, 260, 340, 310, 95]

bills = []
print("Month  Units  Energy    Fixed   Surcharge  Rebate    Total")
for i in range(len(months)):
    u = units_list[i]
    if u < 0:
        print(months[i], "invalid units")
        bills.append(0)
        continue

    energy = 0.0
    if u <= SLAB1_LIMIT:
        energy = u * RATE1
    elif u <= SLAB2_LIMIT:
        energy = SLAB1_LIMIT * RATE1 + (u - SLAB1_LIMIT) * RATE2
    elif u <= SLAB3_LIMIT:
        energy = (SLAB1_LIMIT * RATE1 + (SLAB2_LIMIT - SLAB1_LIMIT) * RATE2
                  + (u - SLAB2_LIMIT) * RATE3)
    else:
        energy = (SLAB1_LIMIT * RATE1 + (SLAB2_LIMIT - SLAB1_LIMIT) * RATE2
                  + (SLAB3_LIMIT - SLAB2_LIMIT) * RATE3 + (u - SLAB3_LIMIT) * RATE4)

    surcharge = 0.0
    rebate = 0.0
    if u > 300:
        surcharge = energy * SURCHARGE_RATE
    if u <= 100:
        rebate = energy * REBATE_RATE

    total = energy + FIXED_CHARGE + surcharge - rebate
    bills.append(total)
    print(f"{months[i]:<6} {u:<6} {energy:<9.2f} {FIXED_CHARGE:<7.2f} {surcharge:<10.2f} {rebate:<9.2f} {total:.2f}")

print("\n=== Month-to-Month Comparison ===")
for i in range(1, len(bills)):
    if bills[i - 1] > 0:
        change = (bills[i] - bills[i - 1]) / bills[i - 1] * 100
        flag = ""
        if change > UNUSUAL_INCREASE:
            flag = "  <-- UNUSUAL INCREASE"
        print(f"{months[i - 1]} -> {months[i]}: {change:+.1f}%{flag}")

highest = 0
for i in range(len(bills)):
    if bills[i] > bills[highest]:
        highest = i
print("\nHighest bill:", months[highest], "=", round(bills[highest], 2))
