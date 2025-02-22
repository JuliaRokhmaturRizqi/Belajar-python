#1. mode write
# dia akan membuat file baru jika tidak ada,
#lalu akan menimpa atau overwrite isinya (menghapus isinya trs diganti data baru )

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("Tata andika")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("Tata.....")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("hehehee")

#enaknya pake write ini kalau filenya (data_1.txt) di delete dan program tersebut dijalankan maka akan langsung bikin file baru (data_1.txt)

#2. mode append 
#with open("data_2.txt",'w',encoding="utf-8") as file:
#    file.write("ketimpa\n")
#
#with open("data_2.txt",'a',encoding="utf-8") as file:
#    file.write("ini kata pake append\n")
#
#with open("data_2.txt",'a',encoding="utf-8") as file:
#    file.write("ini kata pake append 2\n")

#itukan yang diatas kode lama,jadi yang lama gak di overwrite (ditimpa)
#karena kita udah pake 'a' di "with open("data_2.txt",'a',encoding="utf-8") as file:" (kodingan bawah itu loooh)
#karena diawalnya itu pake mode 'w' maka akan menimpa dulu kata 'ketimpa' ngehapus file 'data_2.txt' dulu
#trus kita tambahin;

#pake mode 'a'
#with open("data_2.txt",'a',encoding="utf-8") as file:
#    file.write("ini kata pake append\n")
#with open("data_2.txt",'a',encoding="utf-8") as file:
#    file.write("ini kata pake append 2\n")

#trus tambahhin lagi 
#with open("data_2.txt",'a',encoding="utf-8") as file:
#    file.write("ini kata pake append 2\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("ketimpa\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("ini kata pake append\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("ini kata pake append 2\n")

#3.MODE r+
#dia akan buka terus dia akan menimpa
with open("data_3.txt", "w", encoding="utf-8") as file:
    file.write("datake 3")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("baris ke1\n")
    file.write("baris ke2\n")
    file.write("baris ke3\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    data=file.read()
    print(data)

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("tata\n")#nah ini akan menimpa isi teks berikke1, sesuai dengan panjang data
    

