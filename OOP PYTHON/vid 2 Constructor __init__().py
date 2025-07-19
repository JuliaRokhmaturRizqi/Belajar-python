# OOP adalah pendekatan pemrograman yang berfokus pada objek — bagian-bagian kecil dari program yang punya data (atribut) dan fungsi (method). 
# Di Python, ini sangat berguna untuk membuat kode yang terstruktur, mudah dirawat, dan bisa digunakan ulang.

# ===============================
# Example 1: Constructor tanpa parameter
# ===============================

class hero:  # Membuat class bernama 'hero' (template kosong)
    def __init__(self):  # Constructor default tanpa parameter tambahan
        print("Hallo hehehehe")  # Akan dijalankan saat object dibuat

hero1 = hero()  # Membuat object 'hero1' dari class 'hero'
# Output: Hallo hehehehe

# ===============================
# Example 2: Constructor dengan parameter
# ===============================

class hero:  # Membuat ulang class 'hero'
    def __init__(self, x):  # Constructor dengan 1 parameter tambahan (selain self)
        print("Hallo hehehehe", x)  # Menampilkan nilai dari parameter x

hero1 = hero(10)  # Membuat object 'hero1' dan mengirimkan nilai 10 ke parameter x
# Output: Hallo hehehehe 10

# Keterangan:
# self adalah perwakilan dari object yang dibuat (dalam hal ini: hero1)
# Jadi 'self' akan menunjuk ke 'hero1' di dalam fungsi __init__

# ===============================
# Example 3: Menyimpan data ke atribut object
# ===============================

class hero:  # Membuat class 'hero' sebagai template
    def __init__(self, inputname, inputpower, inputarmor, inputhelth):
        # Menyimpan data ke dalam atribut object
        self.name = inputname      # Atribut 'name' milik object = inputname
        self.power = inputpower    # Atribut 'power' milik object = inputpower
        self.armor = inputarmor    # Atribut 'armor' milik object = inputarmor
        self.helth = inputhelth    # Atribut 'helth' milik object = inputhelth

# Membuat dua object dari class hero dengan data berbeda
hero1 = hero("sniper", 100, 10, 4)      # hero1.name = "sniper", hero1.helth = 4
hero2 = hero("Tata", 9000, 10, 40)      # hero2.name = "Tata", hero2.helth = 40

# Menampilkan atribut tertentu dari object
print(hero1.name)    # Output: sniper
print(hero2.helth)   # Output: 40

# Menampilkan seluruh atribut hero1 dalam bentuk dictionary
print(hero1.__dict__)  # Output: {'name': 'sniper', 'power': 100, 'armor': 10, 'helth': 4}
