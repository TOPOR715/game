import random
class Player:
    def __init__(self):
        self.name = None
        self.age = None
        self.health = 100
        self.stamina = 100
        self.inventory = []
    
    def create_player(self):
        self.name = input("Введите имя персонажа: ")
        self.age = random.randint(18,40)
    
    def __str__(self):
        return f"""\nВы успешно создали персонажа!\nИмя: {self.name},\nВозраст: {self.age}, \nЗдоровье: {self.health}, \nСтамина: {self.stamina}, \nИнвентарь: {self.inventory}"""

# Создаем и настраиваем игрока
player = Player()
player.create_player()
print(player)