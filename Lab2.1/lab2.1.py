'''
Реализуйте приведенное в описании отношение предок

EXAMPLES:
Бабушка Агафья, Брат Андрей
Бабушка Катя, Сводный брат Витя
Дедушка Вася, Сестра Алёнка
Бабушка Агафья, Сводный брат Витя
'''

# в фактах содержатся пары родитель-дети
global facts
facts = {
    "Дедушка Вася": [
        "Папа Максим",
        "Дядя Федор"
    ],
    "Бабушка Агафья": [
        "Папа Максим",
        "Дядя Федор"
    ],
    "Папа Максим": [
        "Брат Андрей",
        "Сестра Алёнка",
        "Сводный брат Витя"
    ],
    "Мама Галя": [
        "Брат Андрей",
        "Сестра Алёнка"
    ],
    "Бабушка Катя": [
        "Мама Галя",
        "Тётя Юля"
    ],
}


# возвращает последний элемент списка
def get_last_element(user_list):
    return user_list[-1]


# возвращает первый элемент списка
def get_first_element(user_list):
    return user_list[0]


# рекрусивная проверка родства: является ли человек 1 предком человека 2
def relationship_test(person_1, person_2):
    if not facts.keys().__contains__(person_1):
        return False
    else:
        if facts[person_1].__contains__(person_2):
            return True

        is_ancestor = False
        for fact in facts[person_1]:
            is_ancestor = relationship_test(fact, person_2)
            if is_ancestor:
                break
        return is_ancestor


if __name__ == '__main__':
    while True:
        # факты, которые вводит пользователь
        user_facts = str(input('\nВведите пару предполагаемых родственников. Например:\nМама Галя, Бабушка Катя\n')) \
            .split(", ")

        # список занесённых в базу людей
        known_names = list(facts.keys())
        for children in facts.values():
            for child in children:
                known_names.append(child)
        known_names = set(known_names)

        # удаляем повторяющиеся факты
        for user_fact in user_facts:
            while user_facts.count(user_fact) > 1:
                user_facts.remove(user_fact)

        # проверяем, содержат ли факты пользователя известные нашей базе факты, и удаляем лишние
        existing_facts = []
        for user_fact in user_facts:
            if user_fact in known_names:
                existing_facts.append(user_fact)
        user_facts = existing_facts

        # рекурсионный вызов для установления факта родства
        if len(user_facts) == 2:
            person1 = get_first_element(user_facts)
            person2 = get_last_element(user_facts)

            if relationship_test(person1, person2):
                print(person1, "является предком", person2)
            else:
                print(person1, "не является предком", person2)
        else:
            print("Введите ПАРУ предполагаемых родственников, занесённых в базу:", known_names)

        existing_facts.clear()