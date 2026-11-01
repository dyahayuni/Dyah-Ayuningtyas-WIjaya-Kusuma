favorite_places = {
    'doyoung': ['seoul', 'tokyo', 'new york'],
    'jihoon': ['paris', 'london', 'berlin'],
    'jaehyuk': ['sydney', 'melbourne', 'brisbane']
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place.title()}")