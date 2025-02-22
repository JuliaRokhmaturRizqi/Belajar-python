#Sendy Firmansyah (2355202057), Indra Lesmana (2355202073)

#PROGRAM TEST UJI KOMPETENSI SEDERHANA

#HALAMAN AWAL
print('''
=====================================================






                     PROGRAM
            TEST UJI KOMPETENSI SEDERHANA
            







======================================================
''')
lanjut = str(input ("Tekan Enter Untuk Lanjut"))
if lanjut == "":
    next
else :
    quit()
#END HALAMAN AWAL

#FORM LOGIN
print('''
_======================================================_
|    SILAHKAN REGISTRASI AKUN TERLEBIH DAHULU          |
========================================================
''')
nama = str(input ("Masukan Nama : " ))
nim = str(input (" Masukan NIM : "))
password = str(input (" Buat Password : "))
print("\n============================================================")

print('''
_======================================================_
<             <<< REGSTRASI BERHASIL >>>              >
========================================================
''')
print("             Silahkan Login Ke Akun Anda\n")
a = nama
b = nim
c = password
while True:
    a = str(input(" Masukkan Nama        : "))
    b = str(input(" Masukan NIM         : "))
    c = str(input(" Masukkan Password : "))
    if a != nama or b != nim or c != password:
        print("\n==========================================================")
        print('''
_==============================================_
<                XXX LOGIN GAGAL XXX           >
================================================                  
''')
        print("               AKUN TIDAK TERDAFTAR!!!\n"
        "         PASTIKAN DATA YANG ANDA MASUKAN BENAR\n")
        print(" COBA LAGI\n")
        continue
    else :
        print("\n============================================================")
        print('''
_================================================_
<             <<< LOGIN BERHASIL >>>             >
==================================================       
''')
        break

lanjut = str(input("Tekan Enter Untuk Lanjut..."))
if lanjut == "":
    next 
else :
    quit()

print('''
------------------------------------------------------------------
------------------------------------------------------------------
''')
#END FORM LOGIN 

#MULAI SOAL 
while True:
    print('''
        _================================================_
        |      SELAMAT DATANG DI PROGRAM TEST UJIAN      |
        ==================================================    
    ''')
    print("Hai", nama)
    print('''
Apakah anda sudah siap mengikuti test?
Sebelum itu kami akan memberitahu anda aturannya terlebih dahulu\n
    1. Anda harus menjawab sepuluh soal pilihan ganda
    2. Total poin jika menjawab soal semua soal dengan benar yakni 100 poin
    3. Soal terdiri dari dua paket yaitu:
       ~ Soal Umum      : 5 soal 70 poin
       ~ Soal Logika    : 5 soal 30 poin
    4. Hasil test akan di keluar setelah uji kompetensi selesai                
''')
    while True : 
        pilih = str(input("Ketik (y) untuk memulai test: "))
        if pilih.lower() == "y":
            break
        else :
            print("pilihan anda salah!!")
            continue


    print('''
        _==================================================_
        |                   <<< SOAL UMUM >>>              |
        ====================================================
    ''')
    print("Jawab Soal Dengan Benar\n")
    print('''
1.  Ketika anda menggunakan komputer berbasis microsoft windows misalnya windows xp , pasangnan tombol [Xtrl]+[c] dapat digunakan untuk:

    A. Menghapus Tulisan
    B. Mengcopy file 
    C. Membuka file
    D. mengatur tulisan ke tengah baris

''')
    pilih_soal1 = str(input("Masukan Pilihan Anda: "))

    print('''
2.  Progran komputer yang dapat digunakan untuk engakses informasi yang ada di internet adalah:

    A. Browser Internet
    B. Microsoft Acces
    C. FTP File Transfer Protocol
    D. HTTP Hypertext Transfer Protocol    
''')
    pilih_soal2 = str(input("Masukan Pilihan Anda: "))

    print('''
3.  Aplikasi internet di bawah dapat digunakan untuk mengirim file kepada orang lain, KECUALI:

    A. Email
    B. Yahoo messanger
    C. Google
    D. Website
''')
    pilih_soal3 = str(input("Masukan Pilihan Anda: "))

    print('''
4.  Kecepatan sebuah komputer di tentukan oleh faktor-faktor sebagai berikut, KECUALI:

    A. Jenis CPU (Misalnya Intel Pentium, Core 2 Duo, AMD Athlon dan lain-lain)
    B. Kapasitas Hardisk
    C. Besarnya Memory (RAM)
    D. Banyaknya program yang sedang dijalankan
    ''')
    pilih_soal4 = str(input("Masukan Pilihan Anda: "))


    print('''
5.  Salah satu software komputer yang digunakan untuk mengolah data nilai siswa, misalnya menghitung rata-rata dan mengurutkan nilai

    A. MS Front Page
    B. MS Windows
    C. MS Excel
    D. MS Word
    ''')
    pilih_soal5 = str(input("Masukan Pilihan Anda: "))

    print('''
        _=====================================================_
        |               <<< SOAL LOGIKA >>>                   |
        =======================================================    
    ''')

    print('''
1.  Benda nama yang lebih berat, kapas 10kg atau besi 10kg?

    A. Kapas 10kg
    B. Besi 10kg
    C. Semua Berat
    ''')
    pilih_soal6 = str(input("Masukkan Pilihan Anda: "))
    print('''
2.  Apakah huruf keempat dalam abjad?

    A. a
    B. d
    C. m
    ''')
    pilih_soal7 = str(input("Masukan Pilihan Anda: "))
    print('''
3.  Jika satu telur butuh merebus 20 menit agar bisa matang,
    berapa lama waktu merebus yang dibutuhkan 10 telur agar
    bisa matang?

    A. 200 menit
    B. 20 menit
    C. Semua salah
    ''')
    pilih_soal8 = str(input("Masukan Pilihan Anda: "))
    print('''
4.  Kalau ada angsa lima, dikali dua. Berapa total semua angsa?
    
    A. 10
    B. 3
    C. 5
    ''')
    pilih_soal9 = str(input("Masukan Pilihan Anda: "))
    print('''
5.  Nasi yang enak buat sarapan biasanya nasi?

    A. Putih
    B. Dingin
    C. Matang
    ''')
    pilih_soal10 = str(input("Masukan Pilihan Anda: "))

    #HITUNG NILAI AKHIR
    s = "Salah"
    b = "Benar"
    benar = 0
    salah = 0
    skor = 0

    #HITUNG SKOR
    if pilih_soal1.upper() == "B":
        skor += 14
    else :
        skor = skor

    if pilih_soal2.upper() == "A":
        skor += 14
    else :
        skor = skor

    if pilih_soal3.upper() == "C":
        skor += 14
    else : 
        skor = skor

    if pilih_soal4.upper() == "B":
        skor += 14 
    else :
        skor = skor

    if pilih_soal5.upper() == "C":
        skor += 14 
    else :
        skor = skor 

    if pilih_soal6.upper() == "C":
        skor += 6
    else :
        skor = skor 

    if pilih_soal7.upper() == "A":
        skor += 6
    else :
        skor = skor 

    if pilih_soal8.upper() == "A": 
        skor += 6
    else :
        skor = skor 

    if pilih_soal9.upper() == "C":
        skor += 6
    else : 
        skor = skor

    if pilih_soal10.upper() == "C":
        skor += 6
    else :
        skor = skor 
    #END HITUNG SKOR

    #MULAI HITUNG BENAR SALAH
    if pilih_soal1.upper() == "B":
        benar += 1
    else :
        salah += 1

    if pilih_soal2.upper() == "A":
        benar += 1
    else :
        salah += 1 

    if pilih_soal3.upper() == "C":
        benar += 1
    else :
        salah += 1

    if pilih_soal4.upper() == "B":
        benar += 1
    else :
        salah += 1

    if pilih_soal5.upper() == "C":
        benar += 1
    else :
        salah += 1

    if pilih_soal6.upper() == "C":
        benar += 1
    else :
        salah += 1 

    if pilih_soal7.upper() == "A":
        benar += 1
    else :
        salah += 1 

    if pilih_soal8.upper() == "B":
        benar += 1
    else :
        salah += 1

    if pilih_soal9.upper() == "C":
        benar += 1
    else :
        salah += 1

    if pilih_soal10.upper() == "C":
        benar += 1
    else :
        salah += 1
    #END HITUNG BENAR SALAH
    print('''
_================================================_
|               <<< TEST SELESAI >>>             |
==================================================    
    ''')

    lanjut = str(input("Tekan Enter Untuk Lanjut..."))
    if lanjut == "":
        next
    else :
        quit()

    print('''
---------------------------------------------------
---------------------------------------------------
''')
    print("-----------------------------------------------------")
    print("|              <<< HASIL TEST ANDA >>>               |")
    print("-----------------------------------------------------")
    print("| Nama               :", nama,)
    print("| NIM                :", nim,)
    print("| Nilai Anda         :", skor,)

    if skor >= 90 :
        print("| Indeks Nilai       : A+")
    elif skor < 90 and skor >= 85   :
        print("| Indeks Nilai       : A")
    elif skor < 85 and skor >= 80   :
        print("| Indeks Nilai       : A-")
    elif skor < 80 and skor >= 75   :
        print("| Indeks Nilai       : B+")
    elif skor < 75 and skor >= 70   :
        print("| Indeks Nilai       : B")
    elif skor < 70 and skor >= 65   :
        print("| Indeks Nilai       : B-")
    elif skor < 65 and skor >= 60   :
        print("| Indeks Nilai       : C+")
    elif skor < 60 and skor >= 55   :
        print("| Indeks Nilai       : C")
    elif skor < 55 and skor >= 50   :
        print("| Indeks Nilai       : C-")
    elif skor < 50 and skor >= 40   :
        print("| Indeks Nilai       : D")
    else :
        print("| Indeks Nilai       : E")

    print("-----------------------------------------------")
    print("|                <<< Rincian >>>              |")
    print("-----------------------------------------------")
    print("| Jawaban Benar     :", benar,)
    print("| Jawaban Salah     :", salah,)

    print("\n| Soal Umum:")
    if pilih_soal1.upper() == "B":
        print("| 1.",b)
    else :
        print("| 1.",s)
    if pilih_soal2.upper() == "A":
        print("| 2.",b)
    else :
        print("| 2.",s)
    if pilih_soal3.upper() == "C":
        print("| 3.",b)
    else :
        print("| 3.",s)
    if pilih_soal4.upper() == "B":
        print("| 4.",b)
    else :
        print("| 4.",s)
    if pilih_soal5.upper() == "C":
        print("| 5.",b)
    else :
        print("| 5.",s)

    print("\n| Soal Logika:")
    if pilih_soal6.upper() == "C":
        print("| 1.",b)
    else :
        print("| 1.",s)
    if pilih_soal7.upper() == "A":
        print("| 2.",b)
    else :
        print("| 2.",s)
    if pilih_soal8.upper() == "B":
        print("| 3.",b)
    else :
        print("| 3.",s)
    if pilih_soal9.upper() == "c":
        print("| 4.",b)
    else :
        print("| 4.",s)
    if pilih_soal10.upper() == "C":
        print("| 5.",b)
    else :
        print("| 5.",s)
    
    print("-------------------------------------------------")
    print('''
_==============================================_
|       <<< TERIMA KASIH TELAH MENCOBA >>>     |
================================================    
    ''')

    ulang = str(input("Apakah Anda Ingin Mencoba Kembali? (y/t): "))
    if ulang.lower() == "y" :
        continue
    else :
        break
#END MULAI SOAL

