import random
# names_rooms = ["Кухня", "Ванная", "Зал"]
# numers_room = random.random(1, 3)
class Home():
    def __init__(self, num_rooms=None, room_names=None):
        self.room_names = room_names or ["Кухня", "Ванная", "Гостиная", "Спальня"]
        self.num_rooms = num_rooms or random.randint(1, len(self.room_names))
        self.rooms = random.sample(self.room_names, self.num_rooms)  # Добавил эту строку!
    
    def __str__(self):
        return f"Дом ({self.num_rooms} комнат): {', '.join(self.rooms)}"

class box():
    def __init__(self, box1 = None, box2 = None, box3 = None):
        self.box1 = box1 or ["Шкафчик"]
        self.box2 = box2 or ["Холодильник"]
        self.box3 = box3 or ["Коробка"]
        
    def box():
        all_box = []

    def __str__(self):
        return f"В этой комнате {0} хранилищь: {self.box1[0]}, {self.box2[0]}, {self.box3[0]}"

box_rooms = box()
print(box_rooms)