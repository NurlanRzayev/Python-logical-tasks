for i in range(32,128):
    print(chr(i),end='')
    if (i-1)%10==0:#с 32 по 41 10 символов , с 42 по 51 тоже , то есть выполнение условия означает что в строку выведен 10 символ
        print()