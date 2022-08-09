for i in range(2, 17):
    s = 69
    s1 = ''
    while s > 0:
        s1 = str(s % i) + s1
        s //=i
   
    if len(s1) == 4 and int(s1) % 10 == 1:
        print(i)
