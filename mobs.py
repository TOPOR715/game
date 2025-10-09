import random
import json
import os

# Автоматическое создание пути для сохранения в папке скрипта
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_DIR = os.path.join(SCRIPT_DIR, 'save_player')
SAVE_FILE = os.path.join(SAVE_DIR, 'save_player.json')

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
    # Создаем папку, если она не существует
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        print(f"Создана папка для сохранений: {SAVE_DIR}")
    
    with open(SAVE_FILE, 'w', encoding='utf-8') as file:
        json.dump(create_player(), file, ensure_ascii=False, indent=4)
    print(f"Персонаж сохранен в: {SAVE_FILE}")

def look_player():
    if not os.path.exists(SAVE_FILE):
        print("Файл сохранения не найден!")
        return
    
    with open(SAVE_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print("\n=== Данные персонажа ===")
        for key, value in data.items():
            print(f"{key}: {value}")
