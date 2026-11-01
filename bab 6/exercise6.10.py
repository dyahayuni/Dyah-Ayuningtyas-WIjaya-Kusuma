angka_favorit = {
    'doyoung': [7, 11, 15],
    'jihoon': [3, 7, 11],
    'yoshi': [9, 13, 17],
}

for name, numbers in angka_favorit.items():
    print(f"\nAngka favorit {name.title()}:")
    for number in numbers:
        print(f"- {number}")