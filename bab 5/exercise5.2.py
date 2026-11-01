#string = kesetaraan dan ketidaksetaraan
buah = 'anggur'
print(buah == 'anggur') # True
print(buah == 'apel') # False
print(buah != 'apel') # True
print(buah != 'anggur') # False

#method lower()
kota = 'SUKOHARJO'
print(kota.lower() == 'sukoharjo') # True
print(kota.lower() == 'surakarta') # False

#numerik
umur = 18
print(umur == 18) # True
print(umur != 18) # False
print(umur > 18) # False
print(umur < 18) # False
print(umur >= 18) # True
print(umur <= 18) # True
print(umur >= 17) # True
print(umur <= 19) # True

#and dan or
print(umur >= 18 and umur <= 30) # True
print(umur < 18 or umur > 30) # False
print(umur < 18 or umur > 30 or umur == 18) # True
print(umur < 18 or umur > 30 or umur == 19) # False

#item ada di list
jajanan = ['tahu bulat, sotong, cilok, cireng']
print('tahu bulat' in jajanan) # True
print('nasgor' in jajanan) # False

#item tidak ada di list
print('tahu bulat' not in jajanan) # False
print('nasgor' not in jajanan) # True