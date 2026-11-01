pizzas = ['pepperoni', 'margherita', 'hawaiian']

for pizza in pizzas:
    print(f"Saya suka pizza {pizza}.")

print("\nSaya benar-benar suka pizza!")

cubes = []

print("\nKubik 1 sampai 10:")
for value in range(1, 11):
    cubes.append(value ** 3)

for cube in cubes:
    print(cube)

friend_pizzas = pizzas[:]

pizzas.append('four cheese')
friend_pizzas.append('meat lovers')

print("\nPizza favoritku adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit temanku adalah:")
for pizza in friend_pizzas:
    print(pizza)