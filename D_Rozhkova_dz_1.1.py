num = int(input())
if num > 0 and num < 8:
    if num == 6 or num == 7:
        print('Это выходной день!')
    else:
        print('Это будний день!')
else:
    print('Некореектное число, попробуйте еще раз.')