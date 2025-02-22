from. import oprasi

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
            print("tahun harus angka (yyyy)")
            
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