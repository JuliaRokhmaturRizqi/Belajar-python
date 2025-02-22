data=16.023
yah = f"hhhhhh{data:.2f}"
print(yah)

data = 20000.8899889
jadi =f"jadinya ;{data:8.3f}"
print(jadi)

data = 20000.8899889
jadi =f"jadinya ;{data:010.3f}"
print(jadi)

data = 2
data2 = -4
plus =f"jadinya ;{data:+d}"
minus =f"jadinya ;{data2:+d}"
print(plus)
print(minus)

#memformat %

persen = 0.0234
fpersen = f"jadinya ; {persen:%}"
print(fpersen)

persen = 0.0234
fpersen = f"jadinya ; {persen:.3%}"
print(fpersen)

#melakukan oprasi aritmatika
h = 23000
j = 3
formatnya = f'jadinya ;{h*j}'
print(formatnya)

h = 230000000
j = 3
formatnya = f'jadinya ;{h*j:,}'
print(formatnya)

#format angka lain (binary, octal, hexadecimal)
angka = 999
binary = f'binary={bin(angka)}'
octal = f'octal ={oct(angka)}'
hexadecimal = f'hexadecimal ={hex(angka)}'
print(binary)
print(octal)
print(hexadecimal)

import datetime as dt
nama = str(input('nama :'))
tanggal = int(input("masukkan tanggal :"))
Bulan = int(input("masukkan Bulan :"))
tahun = int(input("masukkan tahun :"))

jadi = dt.date(tahun,Bulan, tanggal)
hari_ini = dt.date.today()
print(f'jadi tahun,bulan, dan tanggal lahir anda:{jadi} ')
print(f'hari ini hari ;{hari_ini}')

umur = hari_ini-jadi
print(f'umur anda ;{umur}')

import time
jam_sekarang = time.now
print(jam_sekarang)