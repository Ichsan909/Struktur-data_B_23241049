# tabel kebenaran (logika bolean)
# not and or xor

# NOT

print("****logika NOT****")

x = False
y = not x
print('value x =' , x)
print('*****NOT')
print('value y =' , y)

# OR (semmua bernilai true assal ada true nya)
print("****logika OR****")

x = False
y = False
z = x or y
print('value x =' , z)


x = False
y = True
z = x or y
print('value x =' , z)


x = True
y = False
z = x or y
print('value x =' , z)

x = True
y = True
z = x or y
print('value x =' , z)

# and (semmua bernilai true assal ada true nya)
print("****logika and****")

x = False
y = False
z = x and y
print(x, 'and', y , '=', z)


x = False
y = True
z = x and y
print(x, 'and', y, '=' ,z)


x = True
y = False
z = x and y
print(x, 'and' , y, '=' ,z)

x = True
y = True
z = x and y
print(x, 'and' , y, '=' ,z)

# xor (semmua bernilai true assal ada true nya)
print("****logika xor****")

x = False
y = False
z = x ^ y
print(x, 'xor', y , '=', z)


x = False
y = True
z = x ^ y
print(x, 'xor', y, '=' ,z)


x = True
y = False
z = x ^ y
print(x, 'xor' , y, '=' ,z)

x = True
y = True
z = x ^ y
print(x, 'xor' , y, '=' ,z)



