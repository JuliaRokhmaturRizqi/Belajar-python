from.import database
from.util import random_string
import time

def delete(no_buku):
    try:
        with(open(database.DB_NAME,'r')) as file:
            counter = 0
            while (True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter = no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:

def update(no_buku,data_buku,judul,tahun,penulis,pk,date_add):
    data = database.TAMPLATE.copy()

    data["pk"] = pk
    data["date_add"]= date_add
    data["penulis"]=penulis + database.TAMPLATE["penulis"][len(penulis):]
    data["judul"]=judul + database.TAMPLATE["judul"][len(judul):]
    data["tahun"]=str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str)
    try:
        with (open(database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("error dalam update")

def create(tahun,judul,penulis):

    data = database.TAMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"]= time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"]=penulis + database.TAMPLATE["penulis"][len(penulis):]
    data["judul"]=judul + database.TAMPLATE["judul"][len(judul):]
    data["tahun"]=str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
        
    try:
        with open(database.DB_NAME,'a', encoding="utf-8") as file:
            file.write(data_str)#disini pake 'a' akan menambahkan dibawahnya gak pake 'w' karena a = append dan 'w' adalah write (ngehapus data yang ada)
    except:
        print("data sulit ditambahkan booooooossss.....")



def create_first_data():
    penulis= input("penulis: ")
    judul= input("judul: ")
    while(True):
       try:
           tahun = int(input("tahun\t:"))
           if len(str(tahun)) == 4 :
               break
           else:
               print("angka tidak boleh lebih dari 4 karakter (yyyy)")
       except:
           print("tahun harus angka (yyyy)")

    data = database.TAMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"]= time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"]=penulis + database.TAMPLATE["penulis"][len(penulis):]
    data["judul"]=judul + database.TAMPLATE["judul"][len(judul):]
    data["tahun"]=str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    
    try:
        with open(database.DB_NAME,'w', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("udah lah gagal booooooossss")

def read(**kwargs):
    try:
        with open(database.DB_NAME, 'r') as file:
            content = file.readlines()#Membaca seluruh isi file ke dalam content
            jumlah_buku = len(content)#Menghitung jumlah baris dalam file (jumlah_buku).
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku >= jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("membaca database error")
        return False
    return 
