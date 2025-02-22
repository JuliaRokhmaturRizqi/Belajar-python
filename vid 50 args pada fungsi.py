'''*args'''
#masukkan data/argument
#nah kan misal
def fungsi1(nama, tinggi, berat):
    print(f'{nama} tingginya {tinggi} beratnya {berat}')

fungsi1("hmmmm",160,20)

def fungsi2(data_list):
    data=data_list.copy()
    nama=data_list[0]
    tinggi=data_list[1]
    berat=data_list[2]
    print(f'{nama} tingginya {tinggi} beratnya {berat}')

fungsi2(['tata', 170,50])#kan ribet jika seperti ini, karena hrs pake list
#untuk memasukkan nilai kan ggak bisa langsung fungsi2(tata,170,50) makanya pake list "[]"
#nah kita bikin simpel 

#kenalan *args
def fungsi3(*args):#inputnya akan ngikutin yang fungsi1
    nama=args[0]
    tinggi=args[1]
    berat=args[2]
    print(f'{nama} tingginya {tinggi} beratnya {berat}')

fungsi3(160,20,"hmmm")#gak harus pake list '[]'

#study kasusnya 

def tambah(*baseng):#supaya inputnya bebas dan *args ini gak harus pake kata 'args' 
#nah masuk ke "*baseng" otoomatis akan dinamik ya dia akan ikut berubah (kayak 'nama=args[0]') jadi 9 sesuai "hasil"
#nah jadinya kita bisa tambahin sendiri
    output = 0
    for angka in baseng:#nah "baseng" ini adalah tipenya tuple makanya kita bisa diiterasi
        output += angka
    return output
hasil=tambah(1,2,3,4,5,6,7,8,9)#nah ini input nya bisa berapapun terserah
print(f'hasil ={hasil}')