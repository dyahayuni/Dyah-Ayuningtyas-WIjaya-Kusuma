cities = {
    'surakarta': {
        'country': 'Indonesia',
        'population': 520000,
        'fact': 'dikenal juga dengan nama Solo dan terkenal dengan batiknya',
    },
    'tokyo': {
        'country': 'Jepang',
        'population': 14000000,
        'fact': 'ibu kota Jepang',
    },
    'paris': {
        'country': 'Prancis',
        'population': 2100000,
        'fact': 'rumah bagi Menara Eiffel',
    },
}

for city, info in cities.items():
    print(f"Kota: {city.title()}")
    print(f"  Negara: {info['country'].title()}")
    print(f"  Populasi: {info['population']:,}")
    print(f"  Fakta: {info['fact']}\n")
