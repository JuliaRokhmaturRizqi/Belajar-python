class hero:
    #class variabel
    jumlah=0
    
    def __init__(self, inputname, inputpower, inputarmor, inputhelth):
        #instance variabel
        self.name = inputname
        self.power = inputpower
        self.armor = inputarmor
        self.helth = inputhelth
        hero.jumlah += 1#mengakses variabel di class
        print("membuat object hero dengan nama "+inputname)

hero1 = hero("sniper", 100, 10, 4)    
print(hero.jumlah)  
hero2 = hero("Tata", 9000, 10, 40)   
print(hero.jumlah) 
hero3 = hero("achik",200, 40, 999 )
print(hero.jumlah)

#print(hero1.__dict__)
#print(hero2.__dict__)
#print(hero3.__dict__)

