#package adalah tempat untuk menaruh modul modul kita
import contohPackage.matematika
from contohPackage import fisika
hasil_tambah = contohPackage.matematika.tambah(1,2,3,4,5)
print(f'hasil penjumblahan = {hasil_tambah}')

hasil_kali = contohPackage.matematika.kali(1,2,3)
print(f'hasil perkalian = {hasil_kali}')

hasilgaya=fisika.gaya(2,5)
print(f'hasil gaya ={hasilgaya}')

from contohPackage.fisika import gaya
hasilgaya=gaya(2,5)#kayak gini juga bisa ;)
print(f'hasil gaya ={hasilgaya}')

from contohPackage.fisika import gaya as basing
hasilgaya=basing(2,5)#kayak gini juga bisa ;)
print(f'hasil gaya ={hasilgaya}')
