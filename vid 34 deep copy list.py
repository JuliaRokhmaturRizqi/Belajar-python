data1 = [1,0]
data2 = [2,4]
data_2d = [data1,data2]
data_copy = data_2d.copy()

print(f'data gabungan\n{data_2d}\n')

data3 = data_2d[0]
print(f'data ke tiga \n{data3}\n')

data_ke4 = data_2d[0][0]#ini maksudnya itu "data_2d[0]"" itukan data ke 1 ('[1,0]')
#kemudian data_2d[0] ditambah lagi [0] maka jadi data ke 1 dari "data1" yang berada pada "data_2d
print(f'data ke 1 dari "data1" yang berada pada "data_2d" \n{data_ke4}\n')#kemudian ada '[0]'nya lagi  ('1'-> ' didalam data1')
# mudengkannnn.......?

print(f'address data_2d \t:{hex(id(data_2d))}')
print(f'address data_copy \t:{hex(id(data_copy))}')

print('data member :')# nahkan addressnya sama baik dari yg blm dicopy sm yang sdh dicopy
print(f'address data_2d \t:{hex(id(data_2d[0]))}')# jadi kalau salah satu di ubah datanya maka yang lain juga ikut di ubah
print(f'address data_copy \t:{hex(id(data_copy[0]))}')

















