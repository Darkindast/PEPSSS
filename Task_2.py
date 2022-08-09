for n in range(1, 10000):
    n2 = bin(n)[2:]
    n3 = str(int(n2)//10)
    if n % 2 != 0:
        n3 += '10'
    else:
        n3 += '01'
    n10 = int(n3, 2)
    if n10 == 2017:
        print(n)
        
