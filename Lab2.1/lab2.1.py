"""
Реализуйте приведенное в описании отношение предок
TODO Всех потомков проверять

EXAMPLES:
Бабушка Агафья, Брат Андрей
Бабушка Катя, Сводный брат Витя
Дедушка Вася, Сестра Алёнка
Бабушка Агафья, Сводный брат Витя
"""
import xlrd

# открываем файл
database = xlrd.open_workbook('database2.1.xls', formatting_info=True)

# выбираем активный лист
sheet = database.sheet_by_index(0)

# получаем список значений из всех записей и преобразуем его в словарь
children_names = []
for names_group in [sheet.row_values(i)[1] for i in range(sheet.nrows - 1) if sheet.row_values(i)[1]]:
    children_names.append(names_group.split(", "))

# в фактах содержатся пары родитель-дети
facts = dict(zip(sheet.col_values(0, 0, sheet.nrows - 1), children_names))


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


# рекрусивная проверка родства: является ли человек 1 предком человека 2 в конкретном поколении
def relationship_test(person_1, person_2, required_generation, generation_count):
    if not facts.keys().__contains__(person_1):
        return False
    else:
        if facts[person_1].__contains__(person_2):
            if required_generation == generation_count:
                return True
            else:
                return False

        is_ancestor = False
        for fact in facts[person_1]:
            is_ancestor = relationship_test(fact, person_2, required_generation, generation_count + 1)
            if is_ancestor:
                break
        return is_ancestor


# рекурсивный способ получения всех потомков в заданном поколении
def get_offspring(person, required_generation, generation_count):
    offsprings = []
    if not facts.keys().__contains__(person):
        return offsprings

    if required_generation == generation_count:
        return facts[person]
    else:
        for kid in facts[person]:
            offsprings.append(get_offspring(kid, required_generation, generation_count + 1))
        return offsprings


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

        # рекурсивнный вызов для установления факта родства
        if len(user_facts) == 2:
            person1 = get_first_element(user_facts)
            person2 = get_last_element(user_facts)

            # поколение, которое вводит пользователь
            generation = int(input('\nВведите поколение, в котором желаете получить родственника.\n'))
            if generation is not None:
                if relationship_test(person1, person2, generation, 0):
                    print(person1, "является предком", person2, "в поколении", generation)
                else:
                    print(person1, "не является предком", person2, "в поколении", generation)
            else:
                if relationship_test(person1, person2):
                    print(person1, "является предком", person2)
                else:
                    print(person1, "не является предком", person2)
        elif len(user_facts) == 1:
            person1 = get_first_element(user_facts)

            # поколение, которое вводит пользователь
            generation = int(input('\nВведите поколение, в котором желаете получить родственника.\n'))
            if generation is not None:
                print(get_offspring(person1, generation, 0))
        else:
            print("Введите ПАРУ предполагаемых родственников, занесённых в базу:", known_names)

        existing_facts.clear()
        children_names.clear()
