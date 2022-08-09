n =int(input())
mas = []
for i in range(n):
    mas.append(int(input()))
print(mas)   
for j in range(len(mas)-1):
    for i in range(len(mas)-j-1):
        if mas[i] > 0 and mas[i+1] <0:
            mas[i], mas[i+1] = mas[i+1], mas[i]
        elif mas[i] > 0 and mas[i+1] == 0:
            mas[i], mas[i+1] = mas[i+1], mas[i]
        elif mas[i] == 0 and mas[i+1] < 0:
            mas[i], mas[i+1] = mas[i+1], mas[i]
print(mas)    
    


