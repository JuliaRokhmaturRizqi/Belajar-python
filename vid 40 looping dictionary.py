data_dict = {
    'untuk aa':'aa',
    'untuk 4':4, 
}

for i in data_dict:
    print(i)#yang keluar cmn keynya

#operator untuk mengambil item/iterables

kunci = data_dict.keys()#cara mengambil kuncinya
print(kunci)

print('looping nya........................')
for key in data_dict.keys():# untuk key dalam data_dict (terkusus/hanya untuk bagian keys doang)
    print(data_dict.get(key))#printkan data_dict terkhusus/hanya yang memiliki data yang bernama "key"


valuenya = data_dict.values()
print(valuenya)

for v in data_dict.values():
    print(f'valuenya :{v}')

item = data_dict.items()
print(f'itemnya :\n {item}')


for key, value in data_dict.items():
    print(f'key :{key}\t valuenya :{value}')



