#contoh library
import datetime
data_waktu= datetime.datetime.now() #jadi inikan datetime yang pertama itukan modulnya seddangkan yang kedua adalah classnya
#nah untuk melihatnya klik kanan pada datetime yang kedua (sebagai classnya) terus klik go to referance
#sedangkan now() itu adalah methodnya
print(data_waktu)

from collections import Counter
data = ["1","2","3","1"]
Count=0
for i in data:
    if i == "1":
        Count += 1
print(Count)

#program yang lebih simpel
data2 = ["1","2","3","1"]
data_count=Counter(data2)
print(data_count)
print(data_count['1'])

#baca file
import io
file=io.open("file_text.txt","r")
print(file.read())

#note cobalah explore library pada website https://docs.python.org/3/library/index.html
#good luck ;)