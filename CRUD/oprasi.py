from.import database
from.util import random_string
import time

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

def read():
    try:
        with open(database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("membaca database error")
        return False
    return 
