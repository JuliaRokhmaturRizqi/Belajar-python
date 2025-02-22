import datetime
import random
import string
import os
#fromkey

mahasiswa_tamplete={
    'nama':"nama",
    'nim':"0000000",
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}


data_mahasiswa={}


while True:
    os.system("cls")#untuk windows

    print(f"{'selamat datang':^50}")
    print(f"{'Data Mahasiswa':^50}")
    print('-'*50)
    mahasiswa=dict.fromkeys(mahasiswa_tamplete.keys())#membuat dict kosong dengan keynya itu dari mahasiswa template
    mahasiswa['nama']=input('masukkan nama :')
    mahasiswa['nim']=input('masukkan nim :')
    mahasiswa['sks_lulus']=int(input('maksukkan sks lulus'))
    tahun_lahir=int(input("tahun lahir :"))
    bulan_lahir=int(input("bulan lahir :"))
    tanggal_lahir=int(input("tanggal lahir :"))
    mahasiswa['lahir']=datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)
    
    KEY =''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print("-"*70)
    print(f'{"key ":^10}|{"nama":^17}|{"sks":^7}|{"lahir":^10}')
    print("-"*70)
    for KEY in data_mahasiswa:#dari turorial s ebelumnya
        #inget "key in data_mahasiswa" itu ibarat data_mahasiswa dikotakkin(in) trs kotaknya dikasih nama "key" 
        nama = data_mahasiswa[KEY]['nama']
        nim = data_mahasiswa[KEY]['nim']#yang for semua ini buat yang ditampilin di tabel
        sks = data_mahasiswa[KEY]['sks_lulus']#jadi ini itu menyebut nama,nim,dll yang kemudian dimasukin ke tabel
        lahir = data_mahasiswa[KEY]['lahir'].strftime("%x")
        
        print(f'{KEY:^10}|{nama:^17}|{sks:^7}|{lahir:^10}')
        print("-"*70)
    is_done=input("sudah selesai broh (y/n)?")
    if is_done == "y":
        break



