responses = {}

polling_active = True

while polling_active:
    name = input("\nSiapa namamu? ")
    place = input("Kalau kamu bisa mengunjungi satu tempat di dunia, kamu mau ke mana? ")

    responses[name] = place

    repeat = input("Ada orang lain yang mau menjawab? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Hasil Survei ---")
for name, place in responses.items():
    print(f"{name} ingin mengunjungi {place}.")