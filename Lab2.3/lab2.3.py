'''
TASK:
Разработайте экспертную систему продукционного типа с обратным логическим выводом

Наиболее перспективными являются акции предприятий с низким долгом и высоким или средним
ростом за прошедший год. Также можно покупать акции предприятия со средним долгом и высоким ростом.

Низкий долг - процент долга не выше 90%;
средний долг – процент долга выше 90%, но не выше 120%.

Низкий рост – с приростом меньше 15%;
средний рост – с приростом не меньше 15% и не больше 40%;
высокий рост – с приростом выше 40%

EXAMPLES:
80, 42
100, 50
0, 40
120.01, 100
'''

# в фактах содержатся пары параметр - верхняя и нижняя границы
global facts
facts = {
    "долг": [
        {
            "низкий": [0.00, 90.00],
            "средний": [90.01, 120.00],
            "высокий": [120.01, float('inf')]
        }
    ],
    "рост": [
        {
            "низкий": [0.00, 14.99],
            "средний": [15.00, 40.00],
            "высокий": [40.01, float('inf')]
        }
    ]
}

# пары долг-рост наилучших вариантов для покупки
global best_choices
best_choices = [
    ["средний", "высокий"],
    ["низкий", "высокий"],
    ["низкий", "средний"]
]


# возвращает последний элемент списка
def get_last_element(user_list):
    return user_list[-1]


# возвращает первый элемент списка
def get_first_element(user_list):
    return user_list[0]


# проверка на то, представляет ли собой факт число типа float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# сделать вывод о том. какой тип роста/долга представляет собой текущая величина
# иными словами - провести поиск значения в словаре и получить его ключ
def conclude(item_to_search_for, dictionary):
    for key in dictionary:
        value = dictionary[key]
        if value[0] <= item_to_search_for <= value[1]:
            conclusion.append(key)


if __name__ == '__main__':
    while True:
        # факты, которые вводит пользователь
        user_facts = str(input('\nВведите процент долга и роста через запятую, например:\n80, 42\n')) \
            .split(", ")

        # проверяем, являюется ли факты пользователя числами, и удаляем лишние
        existing_facts = []
        for user_fact in user_facts:
            if is_float(user_fact):
                existing_facts.append(float(user_fact))
        user_facts = existing_facts

        # выводы, сделанные на основе фактов
        conclusion = []

        # поиск значений в базе фактов для получения типа долга/роста
        if len(user_facts) == 2:
            debt = get_first_element(user_facts)
            growth = get_last_element(user_facts)

            for types in facts["долг"]:
                conclude(debt, types)

            for types in facts["рост"]:
                conclude(growth, types)

            # делаем вывод на основе типов долга/роста
            if best_choices.__contains__(conclusion):
                print("Можно вложиться в акции предсприятия с долгом", debt, "% и ростом", growth, "%")
            else:
                print("Не стоит вкладываться в акции предсприятия с долгом", debt, "% и ростом", growth, "%")

        # если у нас нет информации о фактах пользователя, то выводим соответствующее сообщение
        else:
            print("I don't have enough information")

        existing_facts.clear()
        conclusion.clear()
