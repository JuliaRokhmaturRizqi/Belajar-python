data = [1,2,3,4,5]
for i in data:
    print(i)

# while = ketika
angka = 0
print(f'angka sekarang -> {angka}')
while angka < 5:
    angka += 1 #maksudnya itu berarti angka 0+1 kemudian di + 1 lagi, dan seterusnya 
    #sampai < 5 (dimana itukan artinya false) dan jika false maka udh engk ngeprint lagi alias udh break (ini oprasi asigment)
    print(f'angka sekarang ->{angka}')
print('cukup!\n')

angka1 = 0
while angka1 < 6 :
    angka1 += 1
    hasilnya = "*"*angka1
    print(hasilnya.center(10))

angka2 = 6
while angka2 > 0 :
    angka2 -= 1
    hasilnya = "*"*angka2
    print(hasilnya.center(10))