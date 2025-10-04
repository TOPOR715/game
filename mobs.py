import random
import json
def Igrok():
    Player_create = {
        "Name": None,
        "Age": None,
        "HP": 100,
        "Stamina": 100,
        "LVL": 1
    }
    return Player_create

def create_player():
    player = Igrok()
    player["Name"] = input("Введите имя персонажа: ")
    player["Age"] = random.randint(18, 40)
    print(f"\nПерсонаж создан: \nИмя: {player['Name']}\nВозраст: {player['Age']} лет\nВаш уровень: {player['LVL']}")
    return player

def save_player():
    with open('D:\python_cod\game\saves\save_player.json', 'w', encoding='utf-8') as file:
        json.dump(create_player(), file, ensure_ascii=False, indent=4)

def look_player():
    with open('D:\python_cod\game\saves\save_player.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data)
