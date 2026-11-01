sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ayam', 'keju', 'pastrami']
finished_sandwiches = []

print("Maaf, deli kehabisan pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Saya membuat sandwich {current_sandwich} kamu.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich)