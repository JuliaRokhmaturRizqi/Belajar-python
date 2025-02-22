'''Latihan funsi'''

import os

# program menghitung luas dan keliling

#membuat header program
os.system("cls")
#os.system("cls")
print(f"{'PROGRAM MENGHITUNG LUAS dan KELILING':^40}")
print(f"{'PERSEGI PANJANG':^40}")
print(f"{'-'*40:^40}")


#Main
while True:
    #input user
    panjang=int(input("masukkan panjang ="))
    lebar=int(input('masukkan lebar ='))
    keliling=panjang*2+lebar*2
    luas=panjang*lebar
    print(f"keliling = {keliling}")
    print(f"Luas = {luas}")
    konfirmasi=str(input("udah selesai bro (y/t) ="))
    if konfirmasi == "t":
        break


def main ():
    while True:
        #input user
        panjang=int(input("masukkan panjang ="))
        lebar=int(input('masukkan lebar ='))
        keliling=panjang*2+lebar*2
        luas=panjang*lebar
        print(f"keliling = {keliling}")
        print(f"Luas = {luas}")
        konfirmasi=str(input("udah selesai bro (y/t) ="))
        if konfirmasi == "y":
            break

header()
main()

#cttt perlu di devob lagi huuuuuuuh~....










