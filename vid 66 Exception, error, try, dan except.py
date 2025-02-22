#exception akan terjadi saat prrogram
#mengalami eror saat runtime
#

#contoh sederhana untuk menangkap exception
#input_user = int(input("masukkan angka ; "))
#hasil = 0
#try:
#    hasil = 10/input_user
#except:
#    print("input gak boleh 0")
#print (f"hasil = {hasil}")

#contoh di aplikasi
while(True):
    angka = int(input("masukkan angka pembagi ; "))
    try:
        hasil = 10/angka
        print(f"hasil {hasil}")
        is_done = input("lanjutkan (y/n)? w2")
        if is_done == "n":
            break
    except:
        print("pembagi nol, silahkan masukan input lagi")

print("akhir dari program 1")

#contoh aplikasi untuk membuat file data.txt
try:
    with open("data.txt",'r') as file:
        print(file.read()) 
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt",'w',encoding='utf-8') as file:
        file.write("file baru")

            
print("akhir dari program 2")