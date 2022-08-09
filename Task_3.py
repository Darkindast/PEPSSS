mas = [int(i) for i in input().split()]
print(mas)
maxx = 0

for i in range(len(mas)-1):
    k = 1
    for j in range(i + 1, len(mas)):
        if mas[i] == mas[j]:
            k += 1
            if k > maxx:
                maxx = k
                f = mas[i]
             
print(f, maxx)
