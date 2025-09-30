class Player:
    def __init__(self):
        self.name = None
        self.age = None
        self.health = 100
        self.stamina = 100
        self.inventory = []
    
    def create_player(self):
        self.name = input("Введите имя персонажа: ")
        self.age = input("Введите возраст персонажа: ")
    
    def __str__(self):
        return f"Игрок: {self.name}, Возраст: {self.age}, Здоровье: {self.health}, Стамина: {self.stamina}, Инвентарь: {self.inventory}"

# Создаем и настраиваем игрока
player = Player()
player.create_player()
print(player)