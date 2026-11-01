# 1. import modul
import exercise_8_16
print(exercise_8_16.make_car('subaru', 'outback', color='blue'))

# 2. import fungsi tertentu
from exercise_8_16 import make_car
print(make_car('subaru', 'outback', color='blue'))

# 3. import fungsi dengan alias
from exercise_8_16 import make_car as mc
print(mc('subaru', 'outback', color='blue'))

# 4. import modul dengan alias
import exercise_8_16 as cf
print(cf.make_car('subaru', 'outback', color='blue'))

# 5. import semua fungsi
from exercise_8_16 import *
print(make_car('subaru', 'outback', color='blue'))