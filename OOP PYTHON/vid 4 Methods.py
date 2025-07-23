# Membuat class bernama 'hero'
class hero:
    # Class variable (berlaku untuk semua objek dari class ini)
    jumblah_hero = 0

    # Constructor / Initializer
    # Fungsi ini otomatis dipanggil saat objek dibuat dari class ini
    def __init__(self, inputname, inputhelth, inputpower, inputarmor):
        # Instance variables (berlaku hanya untuk objek tertentu)
        self.name = inputname      # Menyimpan nama hero
        self.helth = inputhelth    # Menyimpan nilai kesehatan (health)
        self.power = inputpower    # Menyimpan nilai kekuatan (power)
        self.armor = inputarmor    # Menyimpan nilai pertahanan (armor)
        
        # Setiap kali objek baru dibuat, class variable 'jumblah_hero' ditambah 1
        hero.jumblah_hero += 1

    # Method tanpa parameter dan tanpa return (hanya mencetak nama hero)
    def siapa(self):
        print("namaku adalah " + self.name)

    # Method dengan parameter (menambah nilai health sebanyak nilai 'up')
    def helthup(self, up):
        self.helth += up

    # Method dengan return (mengembalikan nilai health saat ini)
    def gethelth(self):
        return self.helth


# Membuat 3 objek dari class hero
hero1 = hero("Tata", 90, 70, 9000)
hero2 = hero("julia", 999, 9999, 99999)
hero3 = hero("julita", 99999, 99, 8099)

# Menampilkan isi variabel milik masing-masing objek (instance variables)
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

# Memanggil method dengan parameter: menambah nilai health hero1 sebanyak 100
hero1.helthup(100)

# Memanggil method tanpa parameter dan tanpa return
hero1.siapa()

# Menampilkan nilai health setelah ditambah (method dengan parameter)
print("method dengan argument")
print(hero1.helth)

# Memanggil method dengan return: mengambil nilai health terkini
print("method dengan return")
print(hero1.gethelth())
