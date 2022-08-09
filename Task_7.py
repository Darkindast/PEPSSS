def pr(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def g(n):
    d = 2
    k = 0
    mas = []
    while d *d < n:
        if n % d == 0:
            if pr(d) == True:
                mas.append(d)
            
            if pr(n//d) == True:
                mas.append(n//d)
        d += 1
    if d * d == n and pr(d) == True:
        mas.append(d)

    for i in range(len(mas)):
        if mas[i] == 3 or mas[i] == 5 or mas[i] == 7:
            k += 1
    if k == 3 and len(mas) == 3:
        return n
k = 0
n = int(input())
for i in range(1, 10**9):
    if g(i) != None:
        k += 1
        print(g(i))
        if k == n:
            break
       
