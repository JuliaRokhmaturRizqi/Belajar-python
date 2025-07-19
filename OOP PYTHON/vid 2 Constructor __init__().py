#OOP adalah pendekatan pemrograman yang berfokus pada objek — bagian-bagian kecil dari program yang punya data (atribut) dan fungsi (method). 
#Di Python, ini sangat berguna untuk membuat kode yang terstruktur, mudah dirawat, dan bisa digunakan ulang.

class hero:#template
    def __init__(self):
        print ("Hallo hehehehe")

hero1 = hero()#akan menjalankan class hero(def__init__...) 

#Example 2
class hero:#template
    def __init__(self, x):
        print ("Hallo hehehehe", x)

hero1 = hero(10)#akan menjalankan class hero(def__init__...) 
#outputnya 'Hallo hehehehe 10'
#fungsi dari 'self' itu sebagai 'hero1' dari 'hero1 = hero(10)'

#Example 3 
class hero:#template
    def __init__(self, inputname, inputpower, inputarmor, inputhelth):
        self.name = inputname
        self.power = inputpower
        self.armor = inputarmor
        self.helth = inputhelth

hero1 = hero ("sniper", 100, 10, 4)
hero2 = hero ("Tata", 9000, 10, 40)

print(hero1.name)
print(hero2.helth)

print(hero1.__dict__)