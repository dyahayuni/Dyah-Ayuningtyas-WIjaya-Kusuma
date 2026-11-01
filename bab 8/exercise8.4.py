def make_shirt(size='L', message='I love Python'):
    print(f"Ukuran kaos: {size}. Tulisan di kaos: '{message}'.")


make_shirt()                                  # large, pesan default
make_shirt(size='M')                          # medium, pesan default
make_shirt('S', 'Belajar itu seru')           # ukuran dan pesan lain