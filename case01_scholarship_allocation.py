# Case Study 1: University Scholarship Allocation
# Applicant tuple: (id, name, aggregate %, [subject marks], attendance %, annual income)

MIN_AGGREGATE = 75
MIN_SUBJECT = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

applicants = [
    ("S101", "Anil",   88.5, [85, 90, 91, 88], 92, 150000),
    ("S102", "Bhavya", 88.5, [80, 95, 92, 87], 92, 120000),
    ("S103", "Charan", 72.0, [70, 75, 68, 75], 90, 100000),
    ("S104", "Divya",  91.0, [95, 88, 92, 89], 70, 90000),
    ("S105", "Eswar",  84.0, [90, 35, 88, 83], 85, 200000),
    ("S106", "Farah",  80.0, [78, 82, 80, 80], 88, 450000),
    ("S107", "Gopi",   88.5, [86, 89, 90, 89], 92, 120000),
    ("S108", "Harini", 79.5, [75, 80, 82, 81], 95, 250000),
]

eligible = []
print("=== Eligibility Check ===")
for app in applicants:
    sid, name, agg, marks, att, income = app   # tuple unpacking
    reasons = []
    if agg < MIN_AGGREGATE:
        reasons.append("aggregate below " + str(MIN_AGGREGATE))
    for m in marks:
        if m < MIN_SUBJECT:
            reasons.append("subject mark " + str(m) + " below " + str(MIN_SUBJECT))
            break
    if att < MIN_ATTENDANCE:
        reasons.append("attendance below " + str(MIN_ATTENDANCE))
    if income > MAX_INCOME:
        reasons.append("income above " + str(MAX_INCOME))

    if len(reasons) == 0:
        eligible.append(app)
        print(sid, name, "-> ELIGIBLE")
    else:
        print(sid, name, "-> REJECTED:", "; ".join(reasons))

# Ranking: higher aggregate, then higher attendance, then lower income, then name (A-Z)
n = len(eligible)
for i in range(n - 1):
    for j in range(n - 1 - i):
        a = eligible[j]
        b = eligible[j + 1]
        key_a = (-a[2], -a[4], a[5], a[1])
        key_b = (-b[2], -b[4], b[5], b[1])
        if key_a > key_b:
            eligible[j] = b
            eligible[j + 1] = a

print("\n=== Final Ranked List ===")
print("Rank  ID    Name     Agg    Att   Income")
rank = 1
for app in eligible:
    sid, name, agg, marks, att, income = app
    print(f"{rank:<5} {sid:<5} {name:<8} {agg:<6} {att:<5} {income}")
    rank += 1
