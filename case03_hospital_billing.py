# Case Study 3: Hospital Billing and Patient Classification
# Patient tuple: (name, age, consultation, diagnostic, treatment, insured)

MAX_BILL_LIMIT = 500000
SENIOR_AGE = 60
SENIOR_CONCESSION = 0.10        # 10% on total
INSURED_CONCESSION = 0.20       # 20% on treatment charges
CHILD_AGE = 5
CHILD_CONSULT_FREE = True

patients = [
    ("Ravi",   65, 500, 2500, 20000, True),
    ("Sita",   30, 400, 1800, 6000,  False),
    ("Baby K", 3,  600, 1000, 3000,  False),
    ("Mohan",  45, 500, -200, 5000,  False),   # invalid (negative charge)
    ("Latha",  52, 700, 15000, 90000, True),
    ("Kumar",  70, 500, 8000, 600000, False),  # exceeds billing limit
]

print("=== Hospital Bills ===")
for p in patients:
    name, age, consult, diag, treat, insured = p

    if consult < 0 or diag < 0 or treat < 0 or age < 0:
        print(f"{name}: INVALID - negative value found")
        continue

    gross = consult + diag + treat
    if gross > MAX_BILL_LIMIT:
        print(f"{name}: INVALID - bill {gross} exceeds limit {MAX_BILL_LIMIT}")
        continue

    concession = 0.0
    if age < CHILD_AGE and CHILD_CONSULT_FREE:
        concession = concession + consult
    if insured:
        concession = concession + treat * INSURED_CONCESSION
    if age >= SENIOR_AGE:
        concession = concession + (gross - concession) * SENIOR_CONCESSION

    net = gross - concession

    if net <= 5000:
        category = "Basic"
    elif net <= 25000:
        category = "Standard"
    else:
        category = "Premium"

    if net > 50000:
        policy = "Instalment plan (3 parts of " + str(round(net / 3, 2)) + ")"
    elif net > 25000:
        policy = "50% advance payment"
    else:
        policy = "Full payment at discharge"

    print(f"\nPatient: {name} (Age {age})")
    print(f"  Gross: {gross:.2f}   Concession: {concession:.2f}   Net: {net:.2f}")
    print(f"  Category: {category}   Payment policy: {policy}")
