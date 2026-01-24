v = [10,30,40,54,89]
print(v[0])
print(v[3])
print(v[-2])
print(v[:])
print(v[1:])
print(v[:3])
print(v[2:4])
v[3] = 100
print(v)
for x in v:
    if x >= 40:
        print(x)
v.append(500)
v.append(600)
v.append(700)
print(v)
v.extend([8,10])
print(v)
v.insert(1,100)
print(v)
v.pop() # remove o ultimo dado
print(v)
print(v[0]) #primeiro elemento
print(v[-1]) #ultimo elemento
for x in v:
    if x % 2==0:
        print(x)
    else: print(x%2)
v.pop()
print(v)
