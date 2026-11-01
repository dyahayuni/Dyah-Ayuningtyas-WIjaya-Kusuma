mountains = ['Everest', 'Rinjani', 'Semeru', 'Fuji']

# append, insert
mountains.append('Kilimanjaro')
mountains.insert(1, 'Merapi')
print(mountains)

# len
print(f"Jumlah gunung: {len(mountains)}")

# sorted (sementara) dan sort (permanen)
print(sorted(mountains))
mountains.sort()
print(mountains)

# reverse
mountains.reverse()
print(mountains)

# pop
removed = mountains.pop()
print(f"Dihapus dengan pop: {removed}")

# remove
mountains.remove('Fuji')

# del
del mountains[0]

print(mountains)