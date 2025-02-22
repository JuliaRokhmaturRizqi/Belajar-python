a = [2,3,1,2,3,4]
panjang = len(a)
i = 0
while i < panjang:
    print(f'angka {a[i]}')
    i += 1

#list comprehension
print(f'\n list comprehension')
data = {'tata', 4, 8, 'hmmmm'}
[print(f'data :{i}') for i in data]

for i in data :
    print(f'hmmmm {i}')

# enumarate
print(f'\n enumarete')
datalist = ['aaaa', 33,'bbbbb']

for index, data in enumerate(datalist):
    print(f'index = {index}, data = {data}')

