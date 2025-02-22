data_angka = [1,0,9,4,6,4,3,2,5,9,4,3,2,8,6,7,]
print(f'data angka = {data_angka}')

# count data (untuk menghitung banyaknya suatu data  misal data 4 berapa banyak angka 4 )
jumblah_data2 = data_angka.count(2)
jumblah_data4 = data_angka.count(4)

print(f'jumblah banyaknya angka 2 = {jumblah_data2}\njumblah banyaknya angka 4 = {jumblah_data4}')

# ambil posisi data
data_nama = "tata", "mino", "achik"
data_ke4 = data_angka[3]
print(f'data ke 4 = {data_ke4}')

data_nama.index("tata")#mengambil indeks data
print(f'indeksnya si tata = {data_nama}')

## MENGURUTKAN DATA
data_angka = [1,0,9,4,6,4,3,2,5,9,4,3,2,8,6,7,]
data_nama = ["tata", "mino", "achik"]
print(f'Data sebelum di urutkan = {data_angka}')
print(f'Data sebelum di urutkan = {data_nama}')
data_angka.sort()
data_nama.sort()
print(f'data setelah diurutkan = {data_angka}')
print(f'data setelah diurutkan = {data_nama}')

# balik listnya
data_angka.reverse()
print(f'datanya dibalik = {data_angka}')

data_nama.reverse()
print(f'datanya dibalik = {data_nama}')

data_nama.remove ("mino")#untuk menghapus
print(data_nama)


