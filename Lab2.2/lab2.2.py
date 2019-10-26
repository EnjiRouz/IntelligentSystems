'''
TASK:
Разработайте экспертную систему
продукционного типа с обратным логическим выводом

Если двигатель не заводится, и фары не горят, то сел аккумулятор.
Если засорился бензонасос, то двигатель не заводится.
Если указатель бензина находится на нуле, то двигатель не заводится.
Если указатель бензина находится на нуле, то нет бензина.

Имеют место факты: фары не горят, указатель бензина находится на нуле

EXAMPLES:
сел аккумулятор
'''

# в фактах содержатся пары следствие-причина
global facts
facts = {
    "сел аккумулятор": [
        "двигатель не заводится",
        "фары не горят"
    ],

    "двигатель не заводится": [
        "указатель бензина находится на нуле",
        "засорился бензонасос"
    ],

    "нет бензина": [
        "указатель бензина находится на нуле"
    ]
}


# возвращает последний элемент списка
def get_last_element(user_list):
    return user_list[-1]


# находит возможные причины проблем (составляет объяснения)
def find_explanation(fact):
    reasons = facts.get(fact)
    if len(reasons) >= 1:
        print("\nДля проблемы " + fact + " характерны следующие причины:")
        for reason in reasons:
            print("* " + reason)
        for reason in reasons:
            if reason in facts:
                find_explanation(reason)


if __name__ == '__main__':
    while True:
        # факты, которые вводит пользователь
        user_facts = str(input('\nTell me a fact. Example input:\nсел аккумулятор\n')) \
            .split(", ")

        known_facts = list(facts.keys())

        # удаляем повторяющиеся факты
        for user_fact in user_facts:
            while user_facts.count(user_fact) > 1:
                user_facts.remove(user_fact)

        # проверяем, содержат ли факты пользователя известные нашей базе факты, и удаляем лишние
        existing_facts = []
        for user_fact in user_facts:
            if user_fact in known_facts:
                existing_facts.append(user_fact)
        user_facts = existing_facts

        # рекурсионный вызов для поиска объяснения
        if len(user_facts) >= 1:
            for user_fact in user_facts:
                print("\nОбъяснение проблемы " + user_fact, end=":")
                find_explanation(user_fact)

        # если у нас нет информации о фактах пользователя, то выводим соответствующее сообщение
        else:
            print("Нет информации по данному факту")

        existing_facts.clear()