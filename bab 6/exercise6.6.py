bahasa_favorit = {
    'doyoung': 'python',
    'jihoon': 'java',
    'yoshi': 'c++',
    'jaehyuk': 'javascript',
    'jeongwoo': 'python'
}

people = ['doyoung', 'jihoon', 'yoshi', 'jaehyuk', 'jeongwoo', 'hyunsuk', 'asahi']

for person in people:
    if person in bahasa_favorit:
        print(f"halo {person.title()}, terima kasih telah mengisi polling!^^")
    else:
        print(f"halo {person.title()}, silahkan mengisi polling bahasa pemrograman favoritmu ya!^^")