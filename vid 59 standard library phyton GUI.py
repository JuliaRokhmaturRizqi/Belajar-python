#GUI -> graphical user interface
import tkinter as tk
from tkinter import ttk
window = tk.Tk()#->ini akan bikin opjek yang namanya window
#"tk.Tk()"->ini adalah objek dari GUI "window"
from tkinter.messagebox import showinfo
#jadi sebenarnya program diatas itu ada pada 1 loop, jadi ini tuh
#loop nya terusssss sampai kita close

#init
window.configure(bg="pink")
window.geometry("250x300")
window.resizable(True,True)
window.title("hallooooo")

#variable dan fungsi
NAMA_belakang=tk.StringVar()#jadi 2 ini adalah variabel 
NAMA_DEPAN=tk.StringVar()#sebaiknya ditaruh diatas
#frame input
input_frame=ttk.Frame(window)

#untuk menenmpatkan input kita harus menggunakan :
#penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)
 
#komponen
#1.label
nama_depan_label=ttk.Label(input_frame,text="nama depan")
nama_depan_label.pack  (padx=20,fill="x",expand=True) #jadi untuk nampilinnya kita pake pack  
#jadiiiii pack itu buat nampilin  
#2. entry untuk nam a depan 
nama_depan_entry=ttk.Entry(input_frame,textvariable=NAMA_DEPAN)#jadi nandi inputannya kan masuk kesini karena 'entry' 
nama_depan_entry.pack  (padx=20,fill="x",expand=True) #jadi untuk nampilinnya kita pake pack    
 
#3.label
nama_belakang_label=ttk.Label(input_frame,text="belakang")
nama_belakang_label.pack  (padx=20,fill="x",expand=True) #jadi untuk nampilinnya kita pake pack    
#4 . entry untuk nama belakang 
nama_belakang_entry=ttk.Entry(input_frame,textvariable=NAMA_belakang )#jadi nandi inputannya kan masuk kesini karena 'entry' 
nama_belakang_entry.pack  (padx=20,fill="x",expand=True) #jadi untuk nampilinnya kita pake pack    


def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    print(NAMA_DEPAN.get())#jadi get uni kita bisa tau isi dari "NAMA_DEPAN"
    pesan=f'hallo {NAMA_DEPAN.get()} {NAMA_belakang.get()}'
    showinfo(title="haiiiiiiiii",message=pesan,)


tombol_sapa=ttk.Button(input_frame,text="sapa!",command=tombol_click)
tombol_sapa.pack(padx=10,pady=10,fill="x",expand=True)




window.mainloop() #-> jadi ini kyk while truenya     