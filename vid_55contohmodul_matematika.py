#modul matematika

def tambah(*args):
    hasil=0
    for data in args:
        hasil += data
    return hasil

def kali(*args):
    hasil=1
    for data in args:
        hasil *= data
    return hasil

#def pangkat(fungsi):
#    return lambda fungsi:fungsi**2

def pangkat(n:int):
    return lambda fungsi:fungsi**n



















