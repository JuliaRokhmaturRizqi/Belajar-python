#indexnya  0(-3)   1(-2)     2(-1)       
data =[   "tata",  "achik",  "inoku",]
print(f'data \t\t\t: {data}')

#mengambil data dari list
data_ke1 = data[0]
print(f'data ke 1 \t\t: {data_ke1}')

data_terakhir = data[-1]# misalkan kita enggak tau nih data terakhir itu ke berapa indeksnya maka bisa langsung -1 sebagai indeksnya
print(f'data terakhir adalah \t: {data_terakhir}')

#cara mengambil info jumblah data dalam list
panjang_data = len(data)
print(f'panjang data \t\t: {panjang_data}')

# manipulasi data list

#  menambahkan item pada list
print(f'data sebelum ditambah\t: {data}')
data.insert(0,"cantik")#memasukkan sesuai dengan posisi yang diinginkan
print(f'data sesudah di tambah\t: {data}')

# menambahkan data di akhir list
data.append("mino")
print(f'data ditambah lagi \t: {data}')

# menambahkan list dengan list
data_baru = ["oyongku", "minoku", "noku-noku"]
data.extend(data_baru)
print(f'data gabungan \t\t: {data}')

# merubah data
data[2] ="miung"
print(f'data sesudah dirubah\t: {data}')#coba merubah data ke 3(ke 2 indeksnya)

# mengremove atau delete
data.remove("miung")# kalau namanya enggak susuai dengan data maka akan eror
print(f'data sesudah di remove\t: {data}')

# meremove data paling belakang
data.pop()
print(f'data paling belakang\nyang diremove\t\t: {data}')

