class hero:
    #class variabel
    jumblah_hero=0

    def __init__(self, inputname, inputhelth, inputpower, inputarmor):
        #instance variabel
        self.name = inputname
        self.helth = inputhelth
        self.power = inputpower
        self.armor = inputarmor
        hero.jumblah_hero += 1

    #volid function, method tanpa return
    def siapa(self):
        print("namaku adalah " + self.name)

    #method dengan argument
    def helthup(self,up):
        self.helth += up

    #method dengan return
    def gethelth(self):
        return self.helth

hero1 = hero("Tata", 90, 70, 9000)
hero2 = hero("julia", 999, 9999, 99999)
hero3 = hero("julita", 99999, 99, 8099)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

hero1.helthup(100)

hero1.siapa()

print("method dengan argument")
print(hero1.helth)

print("method dengan return")
print(hero1.gethelth())