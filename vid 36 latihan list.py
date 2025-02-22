print("DATA BUKU")
list_buku=[]
while True:
    judul = input("masukkan judul\t;")
    penulis = input("masukkan penulis;")
    buku = [judul, penulis]
    list_buku.append(buku)
    for halaman, bukunya in enumerate(list_buku):
        print(f'no halaman :{halaman}\tjudul :{bukunya[0]}\tpenulis :{bukunya[1]}')

