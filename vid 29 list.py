#kumpulan data numbers
data_angka = [1,2,3,4,5]
print(data_angka)

#kumpulan data string
data_string = ["tata","achik"]
print(data_string)

#kumpulan data boolean
data_boolean = [True,False,True]
print(data_boolean)

#kumpulan campuran
data_campuran = [1, "tata", True]
print(data_campuran)

#cara alternatif membuat list
data_range = range(1,10,2)#range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop, list comprehention
pake_for = [i for i in range(0,10)]
print(pake_for)

pake_for = [i**2 for i in range(0,10)]#hasilnya di pangkatin 2
print(pake_for)

#membuat list pake for pake if
pake_for_if = [i for i in range(1,10) if i != 5]#jadi limanya ilang
print(pake_for_if)

pake_for_if = [i for i in range(1,10) if i % 2 == 0 ]#jadi ganjilnya ilang
print(pake_for_if)

pake_for_if = [i for i in range(1,10) if i % 2 != 0 ]#jadi genapnya ilang
print(pake_for_if)