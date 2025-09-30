import random
# names_rooms = ["Кухня", "Ванная", "Зал"]
# numers_room = random.random(1, 3)
class Home():
    def __init__(self, num_rooms=None, room_names=None):
        self.room_names = room_names or ["Кухня", "Ванная", "Гостиная", "Спальня"]
        self.num_rooms = num_rooms or random.randint(1, len(self.room_names))
        self.rooms = random.sample(self.room_names, self.num_rooms)  # Добавил эту строку!
    
    def __str__(self):
        return f"🏠 Дом ({self.num_rooms} комнат): {', '.join(self.rooms)}"

home = Home(2, ["Ванная"])
print(home)