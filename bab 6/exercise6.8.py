pet_1 = {
    'animal': 'cat',
    'owner': 'doyoung'
}

pet_2 = {
    'animal': 'dog',
    'owner': 'jihoon'
}

person_3 = {
    'animal': 'hamster',
    'owner': 'jaehyuk'
}

pets = [pet_1, pet_2, person_3]
for pet in pets:
    print(f"Hewan: {pet['animal'].title()}")
    print(f"Pemilik: {pet['owner'].title()}\n")