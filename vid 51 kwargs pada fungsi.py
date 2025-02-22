'''**kwagrs'''
#fungsi biasa
def fungsi (nama, tinggi, berat):
    '''funngsi biasa'''
    print(f'nama= {nama} tinggi= {tinggi} berat= {berat}')

fungsi("tata", 170, 50)

def fungsi (**kwagrs):
    '''funngsi biasa'''
    print(kwagrs)
print(',,,,,,,,,,,,,,,,,,,,,,,,,,')
fungsi(nama="tata", tinggi=170, berat=50)#jadi ini adalah dictionary bisa ambil si keynya exp "nama"
print(',,,,,,,,,,,,,,,,,,,,,,,,,,')
#jadiiiii

def fungsi1 (**kwagrs):
    '''funngsi biasa'''
    nama=kwagrs["nama"]
    berat=kwagrs["berat"]
    tinggi=kwagrs["tinggi"]
    print(f'nama= {nama} tinggi= {tinggi} berat= {berat}')
def fungsi1(**kwagrs):
    print(kwagrs)
fungsi1(nama="tata", tinggi=170, berat=57)
#jadi kita bisa ngasih fungsi dengan kwaygrs, nanti fungsinya kita bisa bikin pake **kwargs itu

#study kasus

def math(*args,**kwagrs):
    output = 0
    if kwagrs["option"] == "penjumblahan":
        for angka in args:
            output +=angka
    if kwagrs["option"] == "perkalian":
        for angka in args:
            output *= angka
    else :
        print('ndak ada')
    return output


hasil = math(1,2,3,4,5,6,7,8,9, option="penjumblahan")
print(f'hasil jumblah {hasil}')
hasil = math(1,2,3,4,5,6,7,8,9, option="perkalian")
print(f'hasil kali {hasil}')

