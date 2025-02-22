import pygame

#init
pygame.init()# fungsi pygame.init() ini seperti menyalakan mesin sebelum kamu mulai bermain atau membuat game.
#variable running game
isRun = True#Selama isRun bernilai True, game akan terus berjalan dalam loop, sehingga objek di layar akan tetap bisa digerakkan dan semua proses dalam loop akan berulang.
#Begitu kamu menekan tombol close di jendela game (yang terdeteksi sebagai event pygame.QUIT), program mengubah nilai isRun menjadi False, dan itu akan menyebabkan loop berhenti. Ketika loop berhenti, permainan berakhir, dan jendela game akan ditutup.

#membuat display surface object
window_panjang = 500
window_lebar = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

#objek gamenya
#posisi
x=150
y=250
#ukuran
panjang = 20
lebar = 20

#kecepatan gerak
speed = 10

while isRun:
    pygame.time.delay(10)
    #user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#pertanyaan ; kenapa quitnya pake huruf kapital? dan jiika pake huruf kecil dia programnya gk bisa di close
            isRun  = False #jadi ini itu breaknya itu di for bukan diwhile
    #kita ambil semua keyboard press
    keys=pygame.key.get_pressed()#jadi ngambil semua yang di ketik atau diketikkan

    #ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed    

    #update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,200,0),(x,y,lebar,panjang))#kita gambar
    
    #render ke display (ini yang paling berat)
    pygame.display.update()#update display untung di render

pygame.quit()#Kalau kamu menekan tombol “tutup” di jendela game (seperti menutup mainanmu), permainan selesai dan kita menyimpan semua mainan dengan rapi (dengan kode pygame.quit()).
