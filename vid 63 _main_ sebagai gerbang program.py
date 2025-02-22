#__main__ adalah top level code enciroment

#__name__ = "__main__"

##__name__ pada file program utama
print(f"nilai __name__ pada file program ini = '{__name__}'")#jadi si __name__ ini akan berubah menjadi main saat kita
#panggil sebagai program utama atau di  file progaram utama

##__name__ pada filr eksternal
import fungsi

#contoh penggunaan __main__

#nah dalam program itu biasanya ada deklarasi
def fungsi_tambah(a:int,b:int)->int:#ini hanya hint bisa dipake bisa engga
    return a+b

#fungsi utama
if __name__ == "__main__":
    angka1=3
    angka2=6
    hasil=fungsi_tambah(angka1,angka2)
    print(f"hasil dari {angka1}+{angka2}={hasil}")

import package#engk ada apa apa
#tapi jika di terminal di ketikkan "python package" maka "___main__.py" yang ada di folder packagae akan 
#terpanggil coba aja dulu