try:
    import random
    from item import *
except:
    print("всё норм")

class Player:
    def __init__(self):
        self.name = None
        self.age = None
        self.health = 100
        self.stamina = 100
        self.inventory = []
    
    def create_player(self):
        self.name = str(input("Введите имя персонажа: "))
        self.age = random.randint(18,40)
    
    def __str__(self):
        return f"""\nВы успешно создали персонажа!\nИмя: {self.name},\nВозраст: {self.age}, \nЗдоровье: {self.health}, \nСтамина: {self.stamina}, \nИнвентарь: {self.inventory}"""  
Player1 = Player()


def Menu():
    while True:
        try:
            print("Меню")
            Menu_input = int(input("""Используйте ввод цифр что-бы управлять\n1. Начать новую игру\n2. Продолжить\n"""))
            if Menu_input == 1:
                print("Создайте своего персонажа")
                Player1.create_player()
                print(Player1)
            elif():
                print("Вы ввели неправильное значение\n")
        except:
            print("Вы ввели неправильное значение, попробуйте снова\n")
Menu()