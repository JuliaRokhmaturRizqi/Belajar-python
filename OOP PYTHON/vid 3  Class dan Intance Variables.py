# =============================
# Contoh Class dan Instance Variable dalam OOP Python
# =============================

# Class hero adalah blueprint untuk membuat object karakter hero
class hero:
    # Class variable --> Variabel yang dimiliki bersama oleh semua object dari class ini
    # Digunakan di sini untuk menghitung berapa banyak object hero yang dibuat
    jumlah = 0

    # Constructor / initializer --> Fungsi khusus yang otomatis dipanggil saat object dibuat
    def __init__(self, inputname, inputpower, inputarmor, inputhelth):
        # Instance variables --> Variabel yang unik untuk setiap object
        # Menyimpan data untuk masing-masing hero
        self.name = inputname       # Nama hero
        self.power = inputpower     # Kekuatan hero
        self.armor = inputarmor     # Pertahanan hero
        self.helth = inputhelth     # Kesehatan (HP) hero

        # Menambahkan jumlah hero setiap kali object baru dibuat
        # Mengakses class variable 'jumlah' melalui nama class 'hero'
        hero.jumlah += 1

        # Memberi informasi bahwa object hero berhasil dibuat
        print("Membuat object hero dengan nama " + inputname)


# Membuat object hero pertama bernama 'sniper'
hero1 = hero("sniper", 100, 10, 4)  # Akan mencetak: Membuat object hero dengan nama sniper
print(hero.jumlah)  # Output: 1 --> karena baru ada 1 hero yang dibuat

# Membuat object hero kedua bernama 'Tata'
hero2 = hero("Tata", 9000, 10, 40)  # Akan mencetak: Membuat object hero dengan nama Tata
print(hero.jumlah)  # Output: 2 --> karena sudah 2 hero yang dibuat

# Membuat object hero ketiga bernama 'achik'
hero3 = hero("achik", 200, 40, 999)  # Akan mencetak: Membuat object hero dengan nama achik
print(hero.jumlah)  # Output: 3 --> karena total 3 hero yang sudah dibuat

# =============================
# Catatan:
# - Class variable 'jumlah' dimiliki bersama oleh semua object dari class hero
# - Instance variable (name, power, armor, helth) adalah milik masing-masing object
# - self mengacu pada object itu sendiri, misalnya self.name pada hero1 berarti hero1.name
# =============================

# Menampilkan isi variabel dari masing-masing object dalam bentuk dictionary (opsional)
# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)
