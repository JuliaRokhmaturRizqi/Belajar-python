def jawabanA():
    while True:
        jawaban = str(input("Masukkan jawaban (a/b/c) :"))
        if jawaban == "a":
            print("benar")
            print("point mu :20")
            point=20
            break
            return point
        elif jawaban == "b":
            print("salah")
            print("point mu :0")
            point=0
            break
            return 0
        elif jawaban == "c":
            print("salah")
            print("point mu :0")
            point=0
            break
            return 0
        else:
            print("inputan salah, silahkan input lagi")
            loop = True

def jawabanB():
    while True:
        jawaban = str(input("Masukkan jawaban (a/b/c) :"))
        if jawaban == "a":
            print("salah")
            print("point mu :0")
            break
            return 0
        elif jawaban == "b":
            print("benar")
            print("point mu :20")
            break
            return 20
        elif jawaban == "c":
            print("salah")
            print("point mu :0")
            break
            return 0
        else:
            print("inputan salah, silahkan input lagi")
            loop = True

def jawabanC():
    while True:
        jawaban = str(input("Masukkan jawaban (a/b/c) :"))
        if jawaban == "a":
            print("salah")
            print("point mu :0")
            break
            return 0
        elif jawaban == "b":
            print("salah")
            print("point mu :0")
            break
            return 0
        elif jawaban == "c":
            print("benar")
            print("point mu :20")
            break
            return 20
        else:
            print("inputan salah, silahkan input lagi")
            loop = True

def kuis_matematika():
    print("==============================")
    print("========= MATEMATIKA =========")
    print("==============================")
    print("1. Berapakah hasil 8+5 ?")
    print("a. 13")
    print("b. 3")
    print("c. 23")
    while True:
        bocoran1 = 2
        print("kesempatan bocoran soal :", bocoran1)
        jawaban_bocoran = str(input("Apakah mau membuka bocoran jawaban (jawab y/t)? :"))
        if jawaban_bocoran == "y":
            bocoran1 = bocoran1-1
            print("jawabannya : 13")
            print("kesempatan bocoran soal :", bocoran1)
            jawabanA()
            poinK1 = jawabanA()
            print("poin mu=", poinK1)
            break
        elif jawaban_bocoran == "t":
            jawabanA()
            poinK1 = jawabanA()
            break
        else:
            loop = True
    print("2. jika sebuah kotak berisi 3 apel dan anda menambahkan 2 lagi. berapa toatal apel didalam kotak ?")
    print("a. 1")
    print("b. 5")
    print("c. 6")
    while True:
        bocoran2 = bocoran1
        print("kesempatan bocoran soal :", bocoran2)
        jawaban_bocoran = str(input("Apakah mau membuka bocoran jawaban (jawab y/t)? :"))
        if jawaban_bocoran == "y":
            print("jawabannya : 5")
            bocoran2 = bocoran2-1
            print("kesempatan bocoran soal :", bocoran2)
            jawabanB()
            poinK2 = jawabanB()
            break
        elif jawaban_bocoran == "t":
            jawabanB()
            poinK2 = jawabanB()
            break
        else:
            loop = True

    print("3. berapakah 4x6 ?")
    print("a. 10")
    print("b. 12")
    print("c. 24")
    while True:
        bocoran3 = bocoran2
        print("kesempatan bocoran soal :", bocoran3)
        jawaban_bocoran = str(input("Apakah mau membuka bocoran jawaban (jawab y/t)? :"))
        if bocoran3 == 0:
            print("Maaf bocoran soal kamu saat ini telah habis")
            jawabanC()
            poinK3 = jawabanC()
            break
        elif jawaban_bocoran == "y":
            print("jawabannya : 5")
            bocoran3 = bocoran3-1
            print("kesempatan bocoran soal :", bocoran3)
            jawabanC()
            poinK3 = jawabanC()
            break
        elif jawaban_bocoran == "t":
            jawabanC()
            poinK3 = jawabanC()
            break
        else:
            loop = True

    print("4. nando memiliki apel sebanyak 3, kemudian ia memberikan apel kepada meimei dan julia masing-masing 1. berapakah jumblah apel nando saat ini ?")
    print("a. 5")
    print("b. 1")
    print("c. 4")
    while True:
        bocoran4 = bocoran3
        print("kesempatan bocoran soal :", bocoran4)
        jawaban_bocoran = str(input("Apakah mau membuka bocoran jawaban (jawab y/t)? :"))
        if bocoran4 == 0:
            print("Maaf bocoran soal kamu saat ini telah habis")
            jawabanB()
            poinK4 = jawabanB()
            break
        elif jawaban_bocoran == "y":
            print("jawabannya : 5")
            bocoran4 = bocoran4-1
            print("kesempatan bocoran soal :", bocoran4)
            jawabanB()
            poinK4 = jawabanB()
            break
        elif jawaban_bocoran == "t":
            jawabanB()
            poinK4 = jawabanB()
            break
        else:
            loop = True

    print("5. Berapakah hasil 10:2 ?")
    print("a. 5")
    print("b. 1")
    print("c. 4")
    while True:
        bocoran5 = bocoran4
        print("kesempatan bocoran soal :", bocoran5)
        jawaban_bocoran = str(input("Apakah mau membuka bocoran jawaban (jawab y/t)? :"))
        if bocoran5 == 0:
            print("Maaf bocoran soal kamu saat ini telah habis")
            jawabanA()
            poinK5 = jawabanA()
            break
        elif jawaban_bocoran == "y":
            print("jawabannya : 5")
            bocoran5 = bocoran5-1
            print("kesempatan bocoran soal :", bocoran5)
            jawabanA()
            poinK5 = jawabanA()
            break
        elif jawaban_bocoran == "t":
            jawabanA()
            poinK5 = jawabanA()
            break
        else:
            loop = True

    print("============ HASIL ============")
    Hasil_akhir = poinK1 + poinK2 + poinK3 + poinK4 + poinK5
    print("Hasil poin kamu :", poinK1, "+", poinK2, "+", poinK3, "+", poinK4, "+", poinK5, "=", Hasil_akhir)


            

kuis_matematika()
    