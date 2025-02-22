import datetime

mahasiswa1 = {
    'nama':'tata',
    'NIM':"12341",
    'sks_lulus': 80,
    'beasiswa':True,
    'lahir':datetime.datetime(2005,7,9)
}


mahasiswa2 = {
    'nama':'achik',
    'NIM':"12342",
    'sks_lulus': 80,
    'beasiswa':True,
    'lahir':datetime.datetime(1995,7,9)
}

mahasiswa3 = {
    'nama':'asep',
    'NIM':"12343",
    'sks_lulus': 90,
    'beasiswa':False,
    'lahir':datetime.datetime(1945,7,9)
}

data_mahasiswa={
    'kunci1':mahasiswa1,
    'kunci2':mahasiswa2,
    'kunci3':mahasiswa3,
}
print("-"*70)
print(f'{"key ":^10}|{"nama":^17}|{"sks":^7}|{"beasiswa":^17}|{"lahir":^10}')
print("-"*70)#tanda "<" itu artinya rata kiri

for mahasiswa in data_mahasiswa:
    key = mahasiswa

    nama= data_mahasiswa[key]['nama']
    nim =data_mahasiswa[key]['NIM']
    sks=data_mahasiswa[key]['sks_lulus']
    beasiswa=data_mahasiswa[key]['beasiswa']
    lahir=data_mahasiswa[key]['lahir'].strftime("%x")#strftime untuk tampilan tgl yang "07/09/05"
    print(f'{key:^10}|{nama:^17}|{sks:^7}|{beasiswa:^17}|{lahir:^10}')
print("-"*70)


