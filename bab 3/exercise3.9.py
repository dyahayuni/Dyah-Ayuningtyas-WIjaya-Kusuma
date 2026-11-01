guests = ['Doyoung', 'Jaehyuk', 'Haruto']

print(f"Halo {guests[0]}, maukah kamu makan malam bersamaku?")
print(f"Halo {guests[1]}, maukah kamu makan malam bersamaku?")
print(f"Halo {guests[2]}, maukah kamu makan malam bersamaku?")

print(f"\n{guests[1]} tidak bisa hadir.\n")

guests[1] = 'Jihoon'

print(f"Halo {guests[0]}, maukah kamu makan malam bersamaku?")
print(f"Halo {guests[1]}, maukah kamu makan malam bersamaku?")
print(f"Halo {guests[2]}, maukah kamu makan malam bersamaku?")

print("\nAku menemukan meja makan yang lebih besar!\n")

guests.insert(0, 'Yoshi')
guests.insert(2, 'Hyunsuk')
guests.append('Asahi')

print(f"Halo {guests[0]}, maukah kamu makan malam bersamaku?")
print(f"Halo {guests[1]}, maukah kamu makan malam bersamaku?")
print(f"Halo {guests[2]}, maukah kamu makan malam bersamaku?")
print(f"Halo {guests[3]}, maukah kamu makan malam bersamaku?")
print(f"Halo {guests[4]}, maukah kamu makan malam bersamaku?")
print(f"Halo {guests[5]}, maukah kamu makan malam bersamaku?")

print(f"\nAku mengundang {len(guests)} orang ke makan malam.")