def make_sandwich(*items):
    print("\nSandwichmu berisi:")
    for item in items:
        print(f"- {item}")


make_sandwich('keju')
make_sandwich('telur', 'tomat', 'selada')
make_sandwich('ayam', 'keju', 'mayones', 'bawang', 'saus')