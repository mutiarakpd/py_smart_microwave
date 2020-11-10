import function
from function import displayWatt, micro

modechoice=0
powerchoice=0
tempchoice=0

print("Pilih menu")
print('1. Microwave')
print('2. Steam')
modechoice=int(input("Masukkan angka = "))
if modechoice==1:
    micro()
    displayWatt()
elif modechoice==2:
    pass


