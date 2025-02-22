#tutorial membaca file external

print(5*"=","membaca file txt",5*"=")

file= open("file_txt.txt", mode="r")
print(f'status read : {file.readable()}')
print(f'status read : {file.writable()}')


#print(file.read())#baca seluruh file

#baca perbaris
print(file.readline(),end="")#baca bari ke 1
print(file.readline(),end="")#baca bari ke 2
print(file.readline())#btw (end="") itu cuman biar akhir di outputnya itu gak ada "/n" nya doang

#baca semua baris sebagai list
#print(file.readlines())

print(f'apakah file sudah diclose? {file.closed}')

file.close()#untuk mengclose file
print(f'apakah file sudah diclose? {file.closed}')

print(5*"=","Salah satu tehnik membaca file txt menggunakan with",5*"=")

with open("file_txt.txt", mode="r") as file:#Jadi pake with ini gak usah ribet ribet pake kode yang diatas
    content = file.readline()#dan otomatis langsung close ketika program yang ada didalam with ini udah selesai
    print(content, end="")
    print(f'apakah file sudah diclose? {file.closed}')

print(f'apakah file sudah diclose? {file.closed}')