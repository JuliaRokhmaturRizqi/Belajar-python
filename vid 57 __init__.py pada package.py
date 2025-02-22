#import package
#hasil=package.matematika.tambah(1,2,3,4,5)
#print(f'hasil tambah={hasil}')->ini semua gak bakal bisa jalan jadi....... harusnya....

#import package.matematika
#hasil=package.matematika.tambah(1,2,3,4,5)
#print(f'hasil tambah={hasil}')

#import package -> tapi kita ingin dibuat seperti ini kodenya, makaaaaaa kita bisa mengaturnya di file init pada folder yang sama (folder 'package")
#hasil=package.matematika.tambah(1,2,3,4,5)
#print(f'hasil tambah={hasil}')

#import sains #naaaah sekarang jalan
#hasil = sains.matematika.basic.tambah(1,2,3,4,5)
#print(f'hasil tambah={hasil}')

#penjelasannya kan jika kita cmn import sains doank(tanpa init) maka gak bisa
#karena hanya berupa folder doank
#nah cara menempelkannya itu berarti kita harus naruh di init (__init.py) biar 
#si matematikanya nempel disains(jd atributnya)

#import sains
#hasil2 = sains.pisika.gaya(4,5)
#print(f'hasil pisika={hasil2}')

#import sains
#hasil2 = sains.matematika.basic.kali(4,5)
#print(f'hasil pisika={hasil2}')

#import sains *
#import sains #naaaah sekarang jalan
#hasil = sains.matematika.basic.tambah(1,2,3,4,5)
#print(f'hasil tambah={hasil}')

#penjelasannya kan jika kita cmn import sains doank(tanpa init) maka gak bisa
#karena hanya berupa folder doank
#nah cara menempelkannya itu berarti kita harus naruh di init (__init.py) biar 
#si matematikanya nempel disains(jd atributnya)

from sains import*

hasil2 = pisika.gaya(4,5)
print(f'hasil pisika={hasil2}')

import sains
hasil2 = matematika.basic.kali(4,5)
print(f'hasil pisika={hasil2}')
