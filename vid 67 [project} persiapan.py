import os # Modul os digunakan untuk mendeteksi sistem operasi dan menjalankan perintah terminal
import CRUD as CRUD # Mengimpor folder/package CRUD dan mengakses fungsinya lewat prefix CRUD

# Program utama hanya akan dijalankan jika file ini dijalankan secara langsung, bukan diimpor sebagai modul
if __name__ == "__main__":
    sistem_oprasi = os.name # Mendeteksi sistem operasi ('posix' untuk Linux/Mac, 'nt' untuk Windows)

    # Membersihkan layar terminal sesuai sistem operasi
    match sistem_oprasi:#match itu untuk mencocokkan dalam hal ini memcocokkan manakah sistem oprasi yang cocok untuk mengclear tampilan terminal atau consolnya
        case "posix":os.system("clear")#linux
        case "nt": os.system("cls")#windows  

    # Tampilan awal program
    print ("SELAMAT DATANG DI PROGRAM")
    print ("DATABASE PERPUSTAKAAN")
    print("==========================")

    # Mengecek apakah file database tersedia, jika tidak maka buat baru
    CRUD.init_console() # Fungsi ini ada di database.py dan akan dipanggil lewat __init__.py

    # Memulai program utama dalam loop
    while (True):
        # Bersihkan layar setiap kali user memilih menu
        match sistem_oprasi:#match itu untuk mencocokkan dalam hal ini memcocokkan manakah sistem oprasi yang cocok untuk mengclear tampilan terminal atau consolnya
            case "posix":os.system("clear")#linux
            case "nt": os.system("cls")#windows

        # Tampilkan menu pilihan
        print ("SELAMAT DATANG DI PROGRAM")
        print ("DATABASE PERPUSTAKAAN")
        print("==========================")
        print ("1. read data")
        print ("2. Create data")
        print ("3. update data")
        print ("4. delete data\n")

        # Input dari pengguna
        user_input=input("masukkan opsi: ")

        # Jalankan aksi sesuai dengan input use
        match user_input:#mencocokkan manakah yang cocok
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        # Menanyakan apakah user ingin keluar dari program
        is_done=input("apakah udah selesai? (y/n)")
        if is_done == "y" or is_done == "Y":
            break

# Penutup program
print("thank you ;)")