person_1 = {
    'first_name': 'doyoung',
    'last_name': 'kim',
    'age': 18,
    'city': 'jakarta'
}

person_2 = {
    'first_name': 'jihoon',
    'last_name': 'park',
    'age': 20,
    'city': 'bandung'
}

person_3 = {
    'first_name': 'jaehyuk',
    'last_name': 'yoon',
    'age': 19,
    'city': 'surabaya'
}

people = [person_1, person_2, person_3]
for person in people:
    print(f"Nama lengkap: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Umur: {person['age']}")
    print(f"Kota: {person['city'].title()}\n")