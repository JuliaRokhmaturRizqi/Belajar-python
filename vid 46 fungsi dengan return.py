'''fungsi dengan kembalian'''

#y =2x + 1
#y = f(x) -> x nya itukan kyk inputannya(argument) yang udah dibahas pada vid 46
# y nya itu outputnya -> nah outputnya itu namanya return

#tamplete fungsi dengan kembalian

def kuadrat(x):
    '''fungsi kuadrat'''
    hmmmmm = x**2
    return hmmmmm
y = kuadrat(3)
print(y)
print(kuadrat(3))
kuadrat(3)#gk tampil

def tambahan(angka1, angka2):
    return angka1+angka2

print(tambahan(100, 100))

#fungsi dengan return banyak
def oprasi_matematika(angka1, angka2):
    tambah = angka1+angka2
    kurang = angka1-angka2
    bagi = angka1-angka2
    return tambah, kurang, bagi

t, k, b = oprasi_matematika(120, 30)

print(f'hasil tambah = {t}')
print(f'hasil kurang = {k}')
print(f'hasil bagi = {b}')