#OOP adalah pendekatan pemrograman yang berfokus pada objek — bagian-bagian kecil dari program yang punya data (atribut) dan fungsi (method). 
#Di Python, ini sangat berguna untuk membuat kode yang terstruktur, mudah dirawat, dan bisa digunakan ulang.

class hero:
    pass


hero1 = hero()#object/intance (instaslate)
hero2 = hero()
hero3 = hero();
#hero1, hero2, dan hero3 adalah object (biasa juga disebut instance dari class hero)

hero1.name = "sniper"
hero1.health = 100
#name dan health adalah atribut milik object hero1

hero2.name = "sven"
hero2.health = 200

hero3.name = "tata"
hero3.health = 9000

print(hero1) #menunjukkan bahwa hero1 adalah objek dari class hero dan disimpan di lokasi memori tertentu.
print(hero1.__dict__) #menunjukkan semua atribut yang dimiliki hero1 dalam bentuk kamus/dictionary.
print(hero1.name) #isi dari atribut name milik object hero1.