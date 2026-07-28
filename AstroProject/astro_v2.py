# Astro-Financial Engine v2.0

def get_eastern_zodiac(year):
    animals = ['Крыса', 'Бык', 'Тигр', 'Кролик', 'Дракон', 'Змея', 'Лошадь', 'Коза', 'Обезьяна', 'Петух', 'Собака', 'Свинья']
    return animals[(year - 4) % 12]

# feat: add requests dependency for API calls
