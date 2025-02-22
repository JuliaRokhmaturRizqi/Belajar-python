print('bisa pakek kutip 1')
print("a \ttap")
print("ppppp   \b backspace")
print('kkkkkkkkkkkkk \nenter')
print(r'semuanya jadi string /kar\t\n ena ada r\:')#row string

#multi line litteral string
print("""
jdjedhnoeidn
nkjxbnkjxn
njxnkjxnk
kkkkkk
""")

#oprasi dan manipulasi string

#1. menyambung string
nama_pertama = "tata"
nama_kedua ='r'
nama_ketiga ='izqi'

namalengkap = nama_pertama+" "+nama_kedua+nama_ketiga
print(namalengkap)

#2. menghitung string
panjang = len(namalengkap)
print("panjang dari" +" "+ namalengkap + "=" + str(panjang))
print("panjang dari ", namalengkap , "=" ,panjang)

#mengecek apakah ada komponen charakter (char) atau string di string
d="d"
status = d in namalengkap #jadi mengecek apakah d itu ada di namalengkap
print("d apakah ada di nama lengkap ?", status)

#=========================================================
a = "julia"
inputan = str(input("cobak tebak huruf :"))
status = inputan in a
if status == True :
    print("benar")
else:
    print("salah")

#mengecek apakah tidak ada komponen charakter (char) atau string di string
d="d"
status = d not in namalengkap #jadi mengecek apakah d itu ada di namalengkap
print("d apakah tidak ada di nama lengkap ?", status)

#=========================================================
a = "julia"
inputan = str(input("cobak tebak huruf :"))
status = inputan not in a
if status == True :
    print("benar")
else:
    print("salah")

#mengulang string
print('wk'*3)

#indexing
print('indeks ke-0 ;', namalengkap[0] )#ingat! indeks mulai dari 0, jadi indeks ke 0 adalah t
print('indeks ke-4 ;', namalengkap[4] )
print('indeks ke- -1 ;', namalengkap[-1] )#bararti disini jika -1 maka itu akan geser ke kiri, namun perulangan 
#misalkan gini tatarizqi kita mau indeksnya itu -1  maka akan mengambul i dengan kata lain mengulang dari i
#bingung? sama, aku juga wkwkwkwk bingung ngomongnya wkwkwkkwkwkwk
print('indeks ke- 1 sampai 3 ;', namalengkap[1:4] ) #kenapa pakai 4? bukannya itu sampai 3 ya?
#karena jika indeksnya sampai 3 maka nilai indeks yang muncul cuman sampai 2 --> (1-2)
print('indeks ke- 1 sampai 5 ;', namalengkap[1:6] )#sekali lagi ingat bahwa sepasi juga ikut dihitung
print('indeks ke- (1,4,7) ;', namalengkap[1:7:2] )#jadi dapat dikatakan bahwa [1:7:2] itu artinya 1 sampai 7 dengan loncat sebanyak 2

#item paling kecil
print("paling kecil :", min(namalengkap))#disini yang paling kecil adalah sepasi
#item paling besar
print("paling besar :", max(namalengkap))#disini jawabannya adlah z karena z itu paling besar dalam urutan abjad

#kalau lebih pahamnya lihat dibawah ini adlah ascii codenya
ascii_code = ord(" ")
print('nilai ascii code untuk sepasi adalah :', ascii_code)

ascii_code = ord("z")
print('nilai ascii code untuk "z" adalah :', ascii_code)

ascii_code = ord("t")
print('nilai ascii code untuk "t" adalah :', ascii_code)

#operator dalam bentuk method
data ='tata ita rizqi'
jumblah = data.count("a")#jumblah huruf a pada "data" = 3
print("jumblah huruf a pada "+ data +'adalah :' + str(jumblah))


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
