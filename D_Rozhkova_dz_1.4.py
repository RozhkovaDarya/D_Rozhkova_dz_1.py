x = (-100,100) 
x != 0
y = (-100,100)
y != 0
num = int(input())
if num == 1:
    print('x = (1, 100), y = (1, 100)')
elif num == 2:
    print('x = (-1, -100), y = (1, 100)')
elif num == 3:
    print('x = (-1, -100), y = (-1, -100)')
elif num == 4:
    print('x = (1, 100), y = (-1, -100)')
else:
    print('Введите число от 1 до 4')
