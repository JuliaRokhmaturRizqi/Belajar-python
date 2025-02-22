from.import oprasi

#def init_console():
#    print("mengecek database")
#    user_str=input("pause")

DB_NAME="data.txt"
TAMPLATE= {
    "pk":"xxxxxx",
    "date_add": "yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME, "r") as  file:
            print("databese tersedia, init done")
    except:
        print("databese tidak ditemukan, silahkan ,membuat databases baru")
        oprasi.create_first_data()
