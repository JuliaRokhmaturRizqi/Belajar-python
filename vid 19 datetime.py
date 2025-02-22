
import datetime as dt
nama = str(input('nama    :'))
tanggal = int(input("tanggal :"))
Bulan = int(input("Bulan   :"))
tahun = int(input("tahun   :"))
print(26*"~")
jadi = dt.date(tahun,Bulan, tanggal)
hari_ini = dt.date.today()
print(f'tanggal lahir :{jadi} ')
print(f'hari ini      :{hari_ini}')
print(26*"=")
umur = hari_ini-jadi
umur1=umur.days
umur_tahun = umur.days//360
uumur_bulan = (umur.days%360) //30 #disini kita menggunakan modulus, yaitu sisa pembagian (6784/360= 18 sisa 304)
print(f'umur1       :{umur1}')
print(f'umur bulan  :{uumur_bulan}')
print(f'jadi imurmu :{umur_tahun}')
print(f'cie ternyata udah {umur1} hidup di didunia')
print(f'.......... SELAMAT ULANG TAHUN ..........')

#import time
#jam_sekarang = time.time()
#print(jam_sekarang)