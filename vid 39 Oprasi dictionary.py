#dictionary = kamus (dalam artian)
# list -> array, menggnakan index 
data_list = ['aa', 4, 0, 'hmmm']

print(data_list)

#dictionary (dict) -> associative array
#identifier -> key
data_dict = {
    'untuk aa':'aa',
    'untuk 4':4, #jangan lupa kasihkoma
}#pengganti list
print(data_dict['untuk aa'])


#untuk mengetahui panjang dictionary
LENDICT = len(data_dict)
print(f'panjang dict : {LENDICT}')

#mengecek key exist atau tidak
key = 'untuk aa'
cek_key = key in data_dict #kunci didalam data_dict
print(f'apakah {key} ada dalam data_dict : {cek_key}')
# inget ya key itu yang kiri value itu yang kanan

#mengakses value (read) dengan get
print(data_dict['untuk aa'])
print(data_dict.get("untuk aa")) #jangan lupa pakai tanda kurung biasa bukan tanda kurung siku
#printkan data_dict yang (get) atau memiliki dengan parameternya ('untuk aa')
print(data_dict.get("untuk ba"))#jikaa key nya salah maka tidak dapat diketahui valuenya (none)

#mengupdate data
data_dict["untuk aa"] = 'diganti aa'# untuk mengganti
print(data_dict)

data_dict.update({'untuk 5': 5})
print(f' data dict = {data_dict}') # untuk menambah

#mendelete data pada dictionary
del data_dict['untuk 4']
print(f'jadi data yang sudah di delete : {data_dict}')



























