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

print("\nMaafff, meja makan baru tidak sampai tepat waktu. Aku cuma bisa ngundang dua orang.\n")

popped_guest = guests.pop()
print(f"Maafff {popped_guest}, aku nggak bisa mengundangmu makan malam.")

popped_guest = guests.pop()
print(f"Maafff  {popped_guest}, aku nggak bisa mengundangmu makan malam.")

popped_guest = guests.pop()
print(f"Maafff {popped_guest}, aku nggak bisa mengundangmu makan malam.")

popped_guest = guests.pop()
print(f"Maafff {popped_guest}, aku nggak bisa mengundangmu makan malam.")

print(f"\n{guests[0]}, kamu masih diundang ke makan malamku!")
print(f"{guests[1]}, kamu masih diundang ke makan malamku!")

del guests[0]
del guests[0]

print(guests)