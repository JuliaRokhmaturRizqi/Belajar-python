'''default argument'''
#def fungsi(argument)
#def fungsi (argument = nilai defaultnya)

#contoh 1
def say_hi(nama = "kamu cantik/gantrng"):
    '''fungsi dengan default argumen'''
    print(f'hai {nama}')
print('contoh 1')
say_hi("tata")
say_hi()

#contoh 2
print('contoh 2')
def say_halo(nama = "kamu cantik/gantrng", pesan = "apa kabar"):
    '''fungsi dengan default argumen'''
    print(f'hai {nama}, {pesan}')
say_halo("tata", "hehehe")
say_halo("tata")

#contoh 3
print('contoh 3')
def pangkat(angka, pangkat):
    hasil=angka**pangkat
#    print(f'hasil {angka} pangkat {pangkat} adalah {hasil}')
    return hasil#ternyata pakek return

print(pangkat(2,3))

hasil=pangkat(pangkat=4,angka=3)#bisa gini
print(hasil)
print(pangkat(pangkat=4,angka=3))#bisa juga gini

#contoh4
print('contoh 4')
def hitung(input1=1, input2=2, input3=3):
    hasil = input1+input2+input3
    return hasil
print(hitung())
print(hitung(input3=9))#kita bisa mengubah data input3
