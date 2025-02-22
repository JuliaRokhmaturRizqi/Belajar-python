# Global dan local scope

nama = "Tata"# <- ini adalah fariabel global dimana kita bisa akses didalam fungsi
#Akses variabel global di dalam fungsi biasa
def fungsi ():
    print(f'fungsi menampilkan tata{nama}')
fungsi()

#akses variabel global didalam loop
for i in range(0,6):
    print(f'menampilkan tata {i}-{nama}')

#intinya "nama(yang fariabel global)" akan hidup dimanapun programnya



#variabel local
#exp fungsi biasa
def fungsi2():
    nama_local="ucup"# <-Variabel "nama_local(local scope)" tak akan bisa diakses di luar fungsi
#print(nama_local) <- Variabel "nama_local(local scope)" tak akan bisa diakses di luar fungsi

print("x"*20)
print('contoh penggunaan')
print("x"*20)

#misal nih
angka=0
def fungsi1(ubah):
    global angka#fungsi ini akan mendapat akses merubah angka
    angka=ubah

print(f'sebelum{angka}')
fungsi1(4)
print(f'sesudah{angka}')

angka=0
nama="tata"
def fungsi1(ubah_angka,ubah_nama):
    global angka#fungsi ini akan mendapat akses merubah angka
    global nama
    angka=ubah_angka
    nama=ubah_nama

print("x"*20)
print(f'sebelum{angka}')
print(f'sebelum{nama}')
fungsi1(4,"julia")
print(f'sesudah{nama}')
print(f'sesudah{angka}')

#nyoba pake perulangan
angka=0
for i in range(0,6):
    angka+=i
print(angka)

angka2=0
if True:
    angka2=9
print(angka2)

#kesimpulannya pada perulangan (for dan if) masih bisa diubah
#jadiiiiiii global cuman bisa dipakai pd fungsi/def



