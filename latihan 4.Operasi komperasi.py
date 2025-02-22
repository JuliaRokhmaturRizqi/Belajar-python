#Operasi komperasi
#setiap hasil dari operasi komperatif itu selalu bernilai booelan
#>,<,>=,<=,==,!=,is, is not
a = 4
b =2

#lebih dari '>'
hasil = a > b
print(a,">", b, hasil )
hasil = b > a
print(b, ">", a,hasil)
hasil = a > 5
print(a, ">", 5, hasil)

#kurang dari '<'
print("___________________")
hasil = a < b
print(a,"<", b, hasil )
hasil = b < a
print(b, "<", a,hasil)
hasil = a < 5
print(a, "<", 5, hasil)

#kurang dari sama dengan '<='
print("___________________")
hasil = a <= b
print(a,"<=", b, hasil )
hasil = b <= a
print(b, "<=", a,hasil)
hasil = a <= 4
print(a, "<=", 5, hasil)

#lebih dari sama dengan '>='
print("_________lebih dari sama dengan__________")
hasil = a >= b
print(a,">=", b, hasil )
hasil = b >= a
print(b, ">=", a,hasil)
hasil = a >= 5
print(a, ">=", 5, hasil)

#sama dengan "=="
print("_________sama dengan__________")
hasil = a==4
print(a,"=",2, hasil)
hasil = a == b
print(a,"=", b,hasil)

#tidak sama dengan "!="
print("__________tidak sama dengan_________")
hasil = a != b
print(a,"!=", b, hasil)
hasil = b != 2
print(b,"!=", 2, hasil)

print("__________is_________")
#is funsinya membandingkan objek
#is
x = 5 # ini adalah assigment membuat objek
y = 5 # x atau pun y itu namanya objek identity
print("nilai x adalah",x,"id =", hex(id(x)))#coba melihat id nya
print("nilai x adalah",y,"id =", hex(id(y)))#coba melihat id nya
#ok mari coba penggunaan is
hasil = x is y
print("x is y", hasil)# jadi bisa dikatankan bahwa is itu membanding kan id nya (x dan y)
hasil = x is 5
print("x is 5", hasil)#jadi is ini engk bisa digunakan pada literal (5 adalah liral) dan lebih baik menggunakan ==
#jadi literal itu bisa dikatakan angka (cuman angka), exp : 4,5,6,2,3,dll. dan Exp: x=2 maka "x" itu bukan literal
x = 5 # ini adalah assigment membuat objek
y = 6
hasil = x is y
print("x is y", hasil)#hasilnya false karena x dan y memiliki id yang beda (lagi pula dilihat aja udh tau kalao angkanya beda)

print("__________is not_________")
x = 5 
y = 5
hasil = x is not y
print("x is not y", hasil)
x = 7 
y = 5
hasil = x is not y
print("x is not y", hasil)# jadi jika literalnya (7 dan 5) beda maka akan true












