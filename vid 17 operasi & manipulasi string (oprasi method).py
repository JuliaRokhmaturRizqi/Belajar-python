#oprasi method itu ada 
# 1. menghitung panjang list len()
#2. menghitung kemunculan nilai count()
#3. menambah nilai baru append()
#4. mencari suatu nilai ke posisi tertentu insert()
#5. membuang nilai tertentu pop()
#6. membuang nilai tertentu remove()
#7. menyambung list extend()
#8. memperbaiki urutan list reverse()
#9. membalikkan urutan list sort()
#10. mencari nilai max max()
#11. mencari nilai min min ()
#12. mencari nilai sum sum() 
#13. isalpha() ---> mengecek semuanya huruf
#14. isalnum() ---> huruf dan angka
#15. isdecimal() ---> angka saja
#16. isspace() ---> spasi,tap,newline \n
#17. istitle() ---> semua kata dengan huruf besar


#penggabungan
data = ['aku', 'tata','dan','julia']#ini adalah list
gabungan = ','.join(data)
print('gabungannya :', gabungan)
gabungan = ' '.join(data)
print('gabungannya :', gabungan)
gabungan = ' mwehehehe... '.join(data)
print('gabungannya :', gabungan)

#split atau memisahkan
data = "akumwehehetatamwehehejuliamwehehe"
print('splitnya adalah', data.split('mwehehe'))

#alokasi data rjust(), ljust(), center()
data ='julia'
print('"',data.rjust(10))#jadi gini, ketika kamu melihat outputnya km akan paham
data ='a'
print('"',data.rjust(10))#bahwa jatah katanya itu 10("----------") yah kurang kebih begitu (rata kanan)
data ='julia'
print('"',data.center(10, "-"))#jadi gini, ketika kamu melihat outputnya km akan paham

data ='julia'
print(data.strip('a'))#strip berfungsi untuk menghilangkan sesuatu misalkan disini itu huruf "a"

