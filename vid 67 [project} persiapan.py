import os
import CRUD as CRUD 
if __name__ == "__main__":
    sistem_oprasi = os.name

    match sistem_oprasi:#match itu untuk mencocokkan dalam hal ini memcocokkan manakah sistem oprasi yang cocok untuk mengclear tampilan terminal atau consolnya
        case "posix":os.system("clear")#linux
        case "nt": os.system("cls")#windows  


    print ("SELAMAT DATANG DI PROGRAM")
    print ("DATABASE PERPUSTAKAAN")
    print("==========================")

    #check database itu ada atau tidak
    CRUD.init_console()

    while (True):
        match sistem_oprasi:#match itu untuk mencocokkan dalam hal ini memcocokkan manakah sistem oprasi yang cocok untuk mengclear tampilan terminal atau consolnya
            case "posix":os.system("clear")#linux
            case "nt": os.system("cls")#windows

        print ("SELAMAT DATANG DI PROGRAM")
        print ("DATABASE PERPUSTAKAAN")
        print("==========================")
        print ("1. read data")
        print ("2. Create data")
        print ("3. update data")
        print ("4. delete data\n")

        user_input=input("masukkan opsi: ")

        match user_input:#mencocokkan manakah yang cocok
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": print("update data")
            case "4": print("delete data")

        is_done=input("apakah udah selesai? (y/n)")
        if is_done == "y" or is_done == "Y":
            break

print("thank you ;)")