rivers = {
    'nile': 'egypt',
    'mekong': 'vietnam',
    'amazon': 'brazil',
}

for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

print("\nNama sungai:")
for river in rivers.keys():
    print(river.title())

print("\nNama negara:")
for country in rivers.values():
    print(country.title())