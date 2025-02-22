family ={
    "ata":"tata",
    "cik":"achik",
    "makcik":"mamak ci"
}

print(family)

family2 = family.copy()

print(f'data ke dua :{family2}\n')
family2['ata']="ita"#cuman mengubah valuenya doank
print(f'data ke dua setelah diubah :{family2}\n')

#pop
datapop = family2.pop('ata')#data pop artinya 'mentransfer'
print(f'data pop :{datapop}')
print(f'data ke dua :{family}')#jadi karena data familynya udah dipop bagian 'ita', maka ita tersebut hilang atau udah di transfer ke data pop

#pop item
data_terakhir=family.popitem()#data item itu = mentransfer data terakhir
print(f'data pop item :{data_terakhir}')
print(f'data family :{family}')







