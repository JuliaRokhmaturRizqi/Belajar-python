a = ['a','b','c']
b = a


a[1] = 'waw'
print(b)# yang di ubah "a"nya tapi "b"nya ikut ke ubah
# itu karena address nya sama
print(f'id nya a = {hex(id(a))}')
print(f'id nya b = {hex(id(b))}')

#maka untuk mengCOPYnya kita gunakan :
c = a.copy()
print(f'jadi ini adalah data C ={c} \ndengan id c = {hex(id(c))}')
print(f'id nya a\t= {hex(id(a))}')
print(f'id nya bt\t= {hex(id(b))}')

print('bedakan idnya')