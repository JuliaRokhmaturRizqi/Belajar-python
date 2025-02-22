'''fungsi dengan argumen (input)'''

def nama_funsi(input):#nah input ini akan masuk ke badan fungsi
    #dibawah ini adalah badan fungsi
    print(f'haloooooooo {input}')


nama_funsi("julia")

def kalkulator(angka1, angka2):
    tambah = angka1 + angka2
    print(f'{angka1}+{angka2}={tambah}')

input1=int(input("masukkan angka pertama "))
input2=int(input("masukkan angka kedua "))

kalkulator(input1, input2)

print("-"*20)

def say_hi(peserta):
    data_peserta = peserta.copy()
    for peserta in data_peserta:
        print(f'hai {peserta}')
anggota =["a","b","c"]
say_hi(anggota)







