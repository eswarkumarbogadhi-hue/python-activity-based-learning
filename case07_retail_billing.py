# Case Study 7: Retail Billing with Multiple Discount Rules
# Item tuple: (name, category, unit price, quantity)

TAX_CATEGORIES = ["food", "clothing", "electronics"]
TAX_RATES      = [0.05, 0.12, 0.18]
MAX_DISCOUNT = 500.0

cart = [
    ("Rice 10kg",   "food",        650,  2),
    ("T-Shirt",     "clothing",    499,  3),
    ("Headphones",  "electronics", 1999, 1),
    ("Biscuits",    "food",        30,   10),
    ("Toy",         "games",       300,  1),   # unknown category -> invalid
]

print(f"{'Item':<12}{'Cat':<12}{'Qty':>4}{'Price':>9}{'Amount':>10}{'Tax%':>6}{'Tax':>9}")
subtotal = 0.0
total_tax = 0.0
for item in cart:
    name, cat, price, qty = item
    pos = -1
    for i in range(len(TAX_CATEGORIES)):
        if TAX_CATEGORIES[i] == cat:
            pos = i
    if pos == -1 or price <= 0 or qty <= 0:
        print(f"{name:<12}** skipped: invalid record **")
        continue
    amount = price * qty
    tax = amount * TAX_RATES[pos]
    subtotal = subtotal + amount
    total_tax = total_tax + tax
    print(f"{name:<12}{cat:<12}{qty:>4}{price:>9.2f}{amount:>10.2f}{TAX_RATES[pos]*100:>6.0f}{tax:>9.2f}")

# threshold discounts on subtotal
if subtotal >= 5000:
    disc_rate = 0.10
elif subtotal >= 2000:
    disc_rate = 0.05
else:
    disc_rate = 0.0

discount = subtotal * disc_rate
capped = False
if discount > MAX_DISCOUNT:
    discount = MAX_DISCOUNT
    capped = True

grand = subtotal - discount + total_tax
print("-" * 60)
print(f"{'Subtotal':<40}{subtotal:>12.2f}")
note = " (capped)" if capped else ""
print(f"{'Discount ' + str(int(disc_rate*100)) + '%' + note:<40}{-discount:>12.2f}")
print(f"{'Total Tax':<40}{total_tax:>12.2f}")
print(f"{'GRAND TOTAL':<40}{grand:>12.2f}")
