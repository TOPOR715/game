try:
    import random
    from item import *
    from mobs import *
except:
    print("Файлы догружены")

def Menu():
    Menu_input = input("""Меню
    Используйте ввод цифр что-бы управлять
    1. Начать новую игру
    2. Продолжить""")



# Создание персонажа
# try:
#     create_player()
# except:
#     print("")