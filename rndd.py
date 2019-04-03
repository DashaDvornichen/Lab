import random

chislo = (random.randint(0, 50))
polzchislo = -1
while polzchislo != chislo:
    polzchislo = int(input("Введите число:"))
    if polzchislo == chislo:
        print("Поздравляю, вы выиграли")
    else:
        if polzchislo > chislo:
            print("Введите число меньше")
        else:
            print("Введите число больше")