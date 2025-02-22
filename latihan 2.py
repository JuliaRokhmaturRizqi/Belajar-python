#input data user
#data yang dimasukkan pasti string
data = input("masukkan data :")
print("data =",data,type(data))
#kalau ingin datanya menjadi integer
integer = int(input("masukkan angka"))
print("data =",integer,"bertipe",type(integer))
#bagaimana dengan boolean
data_bool = bool(input("masukkan data:"))
print("data =",data_bool,"bertipe",type(data_bool))
#jadi jika di inputkan false outputnya tidak menjadi false, 
# untuk itu data boolean tersebut harus di ubah dulu menjadi integer
data_bool = bool(int(input("masukkan data:")))
print("data =",data_bool,"bertipe",type(data_bool))

print("__________________________________________________________________________________")



