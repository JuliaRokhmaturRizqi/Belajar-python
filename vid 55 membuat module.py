#module matematika dengan import
import vid_55contohmodul_matematika

hasil_tambah = vid_55contohmodul_matematika.tambah(1,2,3,4,5,6,7,8,9)
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = vid_55contohmodul_matematika.kali(1,2,3,4,5,6,7,8,9)
print(f'hasil kali = {hasil_kali}')

hasil_pangkat = vid_55contohmodul_matematika.pangkat(5)
print(f'hasil pangkat = {hasil_pangkat(6)}')

print("x"*50)
from vid_55contohmodul_matematika import tambah,kali,pangkat

hasil_tambah = tambah(1,2,3,4,5,6,7,8,9)
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = kali(1,2,3,4,5,6,7,8,9)
print(f'hasil kali = {hasil_kali}')

hasil_pangkat = pangkat(5)
print(f'hasil pangkat = {hasil_pangkat(6)}')

#penggunaan alias atau AS atau disebut juga 'sebagai'

from vid_55contohmodul_matematika import tambah as basing
#from vid_55contohmodul_matematika import * -> ini jika mau mengimpor semua data(exp:tambah,kali, pangakat)

hasil_tambah = basing(1,2)
print(f'hasil tambah = {hasil_tambah}')