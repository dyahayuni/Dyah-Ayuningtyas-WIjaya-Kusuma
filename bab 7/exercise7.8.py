sandwich_orders = ['tuna', 'ayam', 'keju', 'telur']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Saya sedang membuat sandwich {current_sandwich} kamu.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwich yang telah dibuat:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")