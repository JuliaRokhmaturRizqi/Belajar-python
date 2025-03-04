from. import oprasi
def delete_console():
    read_console()
    while(True):
        print("silahkan pilih nomor buku yang akan di didelete")
        no_buku = int(input("masukkan momor buku: "))
        data_buku=oprasi.read(index = no_buku)
        #print(data_buku)
        if data_buku:
            data_break = data_buku.split(',')
            pk=data_break[0]
            date_add=data_break[1]
            penulis=data_break[2]
            judul=data_break[3]
            tahun=data_break[4][:-1]

            #data yang ingin diupdate
            print("\n"+"="*100)
            print("data yang ingin anda hapus")
            print(f"1. judul\t: {judul:.40}")
            print(f"2. penulis\t: {penulis:.40}")#.40 cuma untuk str
            print(f"3. tahun\t: {tahun:4}")
            is_done=input("apakah anda yakin ingin menghapus data? (y/n)")
            if is_done =="y" or "Y":
                oprasi.delete(no_buku)
                break
        else:
            print("nomor tidak falid, silahkan masukkan lagi")

    print("data berhasil dihapus")



def update_console():
    read_console()
    while(True):
        print("silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("masukkan momor buku: "))
        data_buku=oprasi.read(index = no_buku)
        #print(data_buku)
        if data_buku:
            break
        else:
            print("nomor tidak falid, silahkan masukkan lagi")

    data_break = data_buku.split(',')
    pk=data_break[0]
    date_add=data_break[1]
    penulis=data_break[2]
    judul=data_break[3]
    tahun=data_break[4][:-1]#[:-1] karena datanya belakangnyakan ada enter

    while(True):
        #data yang ingin diupdate
        print("\n"+"="*100)
        print("silahkan pilih data apa yang mau di update")
        print(f"1. judul\t: {judul:.40}")
        print(f"2. penulis\t: {penulis:.40}")#.40 cuma untuk str
        print(f"3. tahun\t: {tahun:4}")
        #memilih mode untuk update
        user_option = input("pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1":judul = input("judul\t: ")
            case "2":penulis = input("penulis\t: ")
            case "3":
                while(True):
                    try:
                        tahun = int(input("tahun\t:"))
                        if len(str(tahun)) == 4 :
                            break
                        else:
                            print("angka tidak boleh lebih dari 4 karakter (yyyy)")
                    except:
                        print("tahun harus angka, silahkan masukkan lagi (yyyy)")
            case _: print("index tidak cocok")


        print("data baru anda")
        print(f"1. judul\t: {judul:.40}")
        print(f"2. penulis\t: {penulis:.40}")#.40 cuma untuk str
        print(f"3. tahun\t: {tahun:4}")
        is_done=input("apakah data sudah sesuai? (y/n)")
        if is_done == "y" or is_done == "Y":
            break

    oprasi.update(no_buku,data_buku,judul,tahun,penulis,pk,date_add)


def create_console():
    print("\n\n"+"="*100)
    print("silahkan tambah data buku\n")
    penulis = input("penulis\t:")
    judul = input("judul\t:")
    while(True):
        try:
            tahun = int(input("tahun\t:"))
            if len(str(tahun)) == 4 :
                break
            else:
                print("angka tidak boleh lebih dari 4 karakter (yyyy)")
        except:
            print("tahun harus angka, silahkan masukkan lagi (yyyy)")
            
    oprasi.create(tahun,judul,penulis)
    print("\n berikut adalah data baru anda")
    read_console()



def read_console():
    data_file = oprasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
    #header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    #data
    for urutan,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{urutan+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}" ,end="")
        #".40" -> artinya memberikan spasi sebanyak 40

    #footer
    print("="*100+"\n")