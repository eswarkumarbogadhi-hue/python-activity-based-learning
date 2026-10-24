# Case Study 10: Campus Event Financial Planning
# Fixed costs: venue, equipment, transport
# Per-participant costs: catering, certificate

venue = 25000
equipment = 18000
transport = 7000
catering_per_head = 150
certificate_per_head = 20

expected_participants = 200
registration_fee = 250
sponsorship = 30000

fixed_cost = venue + equipment + transport
variable_per_head = catering_per_head + certificate_per_head
total_cost = fixed_cost + variable_per_head * expected_participants

print("=== Cost Breakdown ===")
print(f"Venue                 : {venue:>8}")
print(f"Equipment             : {equipment:>8}")
print(f"Transport             : {transport:>8}")
print(f"Catering ({expected_participants} x {catering_per_head})   : {catering_per_head * expected_participants:>8}")
print(f"Certificates ({expected_participants} x {certificate_per_head}): {certificate_per_head * expected_participants:>8}")
print(f"TOTAL COST            : {total_cost:>8}")

print("\n=== Funding ===")
need_after_sponsor = total_cost - sponsorship
print(f"Sponsorship           : {sponsorship}")
if need_after_sponsor < 0:
    need_after_sponsor = 0
print(f"Amount to be raised from participants: {need_after_sponsor}")

contribution = need_after_sponsor / expected_participants
print(f"Contribution per participant (to break even): Rs.{contribution:.2f}")

collected = registration_fee * expected_participants
balance = collected + sponsorship - total_cost
print(f"\nAt Rs.{registration_fee} registration fee: collected {collected}, balance {balance}")
if balance >= 0:
    print("Event is financially viable (surplus).")
else:
    print(f"Sponsorship shortfall / deficit: Rs.{-balance}")

print("\n=== Break-even Registration Count ===")
margin_per_head = registration_fee - variable_per_head
if margin_per_head <= 0:
    print("Fee does not cover per-head costs; break-even impossible.")
else:
    amount = fixed_cost - sponsorship
    if amount <= 0:
        count = 0
    else:
        count = amount // margin_per_head
        if amount % margin_per_head != 0:
            count = count + 1
    print(f"Margin per participant = {registration_fee} - {variable_per_head} = {margin_per_head}")
    print(f"Minimum registrations to break even: {count}")
    print("\nParticipants  Income  Cost   Balance")
    for n in range(count - 20, count + 41, 20):
        if n < 0:
            continue
        income = n * registration_fee + sponsorship
        cost = fixed_cost + variable_per_head * n
        print(f"{n:<13} {income:<7} {cost:<6} {income - cost}")
