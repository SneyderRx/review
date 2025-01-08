lim = int(input("Ingrese el límite de los números: "))
lim = lim + 1
listnum = []
listnumnp = []

for i in range(lim):
    listnum.append(i) 

npri = listnum.copy()
npri.remove(0)
npri.remove(1)

for i in range(2,lim):
    n = listnum[i]
    if n != 2 and n != 3 and n != 5 and n!= 7:
        if (n%1==0 and n%n==0) and (n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%9==0):
            npri.remove(n)
        else:
            listnumnp.append(n)

#Encuentra números primos gemelos
# for i in range(2,len(npri)):
#     s = i + 1
#     if s < len(npri):
#         n1 = npri[i]
#         n2 = npri[s]

#     if n2 - n1 == 2:
#         print(f"Números primos gemelos: {n1} {n2}")

strnp = str(npri)
invstrnp = strnp[::-1]
print(npri)
print(strnp)
print(invstrnp)

    
for i in range(len(npri)):
   if npri[i] == strnp[i]:
    listp = npri[i]
    print(listp)

# print(f"Números no primos: {listnumnp}")
# print(f"Números primos: {npri}")
# print(f"Números ingresados: {listnum}")