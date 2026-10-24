# Case Study 6: Railway Fare and Reservation Calculator

classes = ["SL", "3A", "2A", "1A"]
rates   = [0.55, 1.45, 2.10, 3.50]   # Rs per km

distance = 640
travel_class = "3A"
RESERVATION_FEE = 40
# Passenger tuple: (name, age, gender, berth required)
passengers = [
    ("Ramesh", 35, "M", True),
    ("Sunita", 62, "F", True),
    ("Arvind", 66, "M", True),
    ("Meena",  9,  "F", True),
    ("Tiny",   3,  "M", False),
]
hours_before_departure = 30    # used for cancellation

idx = -1
for i in range(len(classes)):
    if classes[i] == travel_class:
        idx = i
if idx == -1:
    print("Invalid class")
else:
    rate = rates[idx]
    # distance slabs: first 200 km full, next 300 km 90%, beyond 500 km 80%
    if distance <= 200:
        base = distance * rate
    elif distance <= 500:
        base = 200 * rate + (distance - 200) * rate * 0.90
    else:
        base = 200 * rate + 300 * rate * 0.90 + (distance - 500) * rate * 0.80

    print(f"Distance {distance} km, Class {travel_class}, Base fare per adult: Rs.{base:.2f}\n")
    print(f"{'Passenger':<10}{'Age':<5}{'Concession':<12}{'Fare':>9}{'Resv':>7}{'Total':>10}")

    grand_total = 0.0
    totals = []
    for p in passengers:
        name, age, gender, berth = p
        concession = 0.0
        if age < 5:
            concession = 1.0            # free if no berth
            if berth:
                concession = 0.5
        elif age < 12:
            concession = 0.5
        elif age >= 60:
            if gender == "F":
                concession = 0.5
            else:
                concession = 0.4

        fare = base * (1 - concession)
        resv = RESERVATION_FEE
        if age < 5 and not berth:
            resv = 0
        total = fare + resv
        totals.append(total)
        grand_total = grand_total + total
        print(f"{name:<10}{age:<5}{str(int(concession*100)) + '%':<12}{fare:>9.2f}{resv:>7}{total:>10.2f}")

    print(f"\nGrand total: Rs.{grand_total:.2f}")

    # Cancellation penalty
    print(f"\nCancellation {hours_before_departure} hours before departure:")
    if hours_before_departure > 48:
        pen_text = "flat Rs.60 per passenger"
        penalty = 60 * len(passengers)
    elif hours_before_departure >= 12:
        pen_text = "25% of fare"
        penalty = grand_total * 0.25
    elif hours_before_departure >= 4:
        pen_text = "50% of fare"
        penalty = grand_total * 0.50
    else:
        pen_text = "no refund"
        penalty = grand_total
    print(f"  Rule: {pen_text}")
    print(f"  Penalty: Rs.{penalty:.2f}   Refund: Rs.{grand_total - penalty:.2f}")
