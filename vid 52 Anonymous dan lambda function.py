print("x"*29)
print('lambda function')
print("x"*29)
#fungsinya agar program kita itu lebih simpel
#exp
def kuadrat(angka):
    return angka**2 #ini adalah fungssi biasa
print(kuadrat(9))

#fungsi lambda
# output = lambda argument: expression
kuadrat2 = lambda angka:angka**2
print(f"hasil lamda kuadrat :{kuadrat2(3)}")

#lambda dengan 2 input
#exp
jijal = lambda angka,pangkat : angka**pangkat
print(f"hasil nyoba lambda berpangkat = {jijal(4,2)}")

#kegunaannya
#exp sorting (pengurutan) untuk list

#exp sorting biasa pake list biasa
list_tata=["aaaa","zzzz","cc"]
list_tata.sort()
print(list_tata)
#exp sorting biasa pakai panjang
list_tata.sort(key=len)
print(list_tata)

#exp fungsi sorting biasa pakai panjang
def tata(input):
    return len(input)
list_tata.sort(key=tata)
print(f'hasil dari fungsi biasa ={list_tata}')

#sort pakai lambda
jijal2=["aaaa","b","ww"]
jijal2.sort(key=lambda jijal2: len(jijal2))
print(f'sort dari lamda {jijal2}')

#filter
angka=[1,2,3,4,5,6,7,8]
angka2=[1,2]
#exp kasus genap

def kurang_dari_lima(angka):
    return angka < 5
data_baru=list(filter(kurang_dari_lima,angka2))#filter itu mengambil angka yang sama
print(f'hasil filter dari fungsi biasa {data_baru}')

data_baru2=list(filter(lambda x:x<5,angka))
print(f'hasil filter dari lambda {data_baru2}')

#aku nyoba buat seleksi/filter buat khusus yg genap doank
data_genap=list(filter(lambda x:(x%2==0),angka))
print(f'kita buat filter untuk angka genap pakai lambda{data_genap}')

#aku nyoba buat seleksi/filter buat khusus yg ganjil doank
data_ganjil=list(filter(lambda x:(x%2!=0),angka))
print(f'kita buat filter untuk angka ganjil pakai lambda{data_ganjil}')

print("x"*29)
print("ANONYMOUS FUNCTION")
print("x"*29)

#currying

#fungsi biasa
def pangkat(angka,pangkat):
    hasil=angka**pangkat
    return hasil

print(f'hasil fungsi b aja{pangkat(4,5)}')

#dengan currying
def pangkat(n):
    return lambda x:x**n
pangkat2=pangkat(2)#pangkat2 ini seakan jadi fungsi cmn gara2 menggunakan def pangkat
print(f'hasil dari pengkat 2 dengan currying ={pangkat2(5)}')
#misal kita seru-seruan buat pangkat 3 dari 5
pangkat3=pangkat(3)
print(f'hasil dari pengkat 3 dengan currying ={pangkat3(5)}')
#pangkat bebas
print(f'hasil dari pengkat bebas dengan currying ={pangkat(5)(4)}')#jadi ini 4**5
