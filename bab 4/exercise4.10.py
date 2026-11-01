cubes = []

for value in range(1, 11):
    cubes.append(value ** 3)

for cube in cubes:
    print(cube)

cubes = [value ** 3 for value in range(1, 11)]

print("Tiga item pertama di list adalah:")
print(cubes[:3])

print("\nTiga item dari tengah list adalah:")
print(cubes[3:6])

print("\nTiga item terakhir di list adalah:")
print(cubes[-3:])