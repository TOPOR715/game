try:
    import random
    from item import *
    from mobs import *
    import json
except:
    print("всё не норм")

def text_menu():
    print("Используйте ввод цифр что-бы управлять")
    print("1. Начать новую игр")
    print("2. Продолжить")
    print("3. Пасмотреть персонажа")


def Menu():
    while True:
        try:
            print("Меню")
            text_menu()
            print("")
            Menu_input = int(input("""Ввод: """))
            if Menu_input == 1:
                print("")
                print("Создайте своего персонажа")
                save_player()
                print("")
            elif():
                print("Вы ввели неправильное значение\n")

            if Menu_input == 3:
                look_player()
        except:
            print("Вы ввели неправильное значение, попробуйте снова\n")
Menu()