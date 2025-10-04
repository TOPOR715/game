try:
    import random
    from item import *
    from mobs import *
    import json
except:
    print("всё не норм")

def Menu():
    while True:
        try:
            print("Меню")
            Menu_input = int(input("""Используйте ввод цифр что-бы управлять\n1. Начать новую игру\n2. Продолжить\nВвод: """))
            if Menu_input == 1:
                print("")
                print("Создайте своего персонажа")
                save_player()
                print("")
            elif():
                print("Вы ввели неправильное значение\n")
        except:
            print("Вы ввели неправильное значение, попробуйте снова\n")
Menu()