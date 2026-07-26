import os
import shutil
import requests
from datetime import datetime

def organize_kitchen_files():
    """Пример сортировки файлов по расширениям"""
    formats = {
        'Images': ['.jpg', '.png', '.jpeg'],
        'Docs': ['.pdf', '.txt', '.html'],
        'Scripts': ['.py', '.sh']
    }
    
    print("--- 1. Сортировка файлов ---")
    for folder in formats.keys():
        if not os.path.exists(folder): os.makedirs(folder)
    
    # Имитация: смотрим файлы в текущей директории
    for file in os.listdir('.'):
        for folder, ext_list in formats.items():
            if any(file.endswith(ext) for ext in ext_list):
                print(f"Файл {file} можно переместить в {folder}")

def check_mobile_status():
    """Получение системной информации (заряд батареи)"""
    print("\n--- 2. Статус системы (Battery) ---")
    try:
        # В среде Colab/Android можно прочитать системные файлы
        with open("/sys/class/power_supply/battery/capacity", "r") as f:
            level = f.read().strip()
            print(f"Заряд Poco C65: {level}%")
    except:
        print("Информация о батарее недоступна в текущем окружении runtime")

def get_daily_quote():
    """Парсинг данных для вдохновения"""
    print("\n--- 3. Вдохновение для кодинга ---")
    try:
        res = requests.get("https://api.quotable.io/random", timeout=5)
        data = res.json()
        print(f'"{data["content"]}" — {data["author"]}')
    except:
        print("Не удалось получить цитату (проверь сеть)")

if __name__ == '__main__':
    organize_kitchen_files()
    check_mobile_status()
    get_daily_quote()
