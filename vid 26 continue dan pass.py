#continue, pass , break
angka = 0
while angka < 5:
    angka += 1
    print (angka)

print(25*"=")
#pass
angka = 0
while angka < 5:
    angka += 1

    if angka == 3:
        print('mwehehehe...')
        pass #ini tidak akan di eksekusi
    else: # bingung?, sama aku juga bingung :(
        print(f'hmmmmm {angka}')
print(25*"=")

contoh1 = 3
if contoh1 > 5 :
    print('yaaaaa')
elif contoh1 < 5 :
    print('yang bener aja')
    pass
else:
    print('hmmmm... ')

#continue

angka = 0
while angka < 5:
    angka += 1
    print(f'hmmmm ke :{angka}')
    if angka == 3:
        print('mwehehehe...')
        continue #akan membuat loop loncat ke step/loop selanjutnya (perulangngan ke 4)
    print('tata')#tanpa memanggil "tata"
print('cukup')
