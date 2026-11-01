def make_shirt(size, message):
    print(f"Ukuran kaos: {size}. Tulisan di kaos: '{message}'.")


make_shirt('L', 'I love Python')                      # argumen posisional
make_shirt(message='Hello World', size='M')           # argumen keyword