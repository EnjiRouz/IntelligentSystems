'''
FACTS:
A plant with stunted growth may have a nitrogen deficiency.
A plant that is pale yellow in color may have a nitrogen deficiency.
A plant that has reddish-brown leaf edges may have a nitrogen deficiency.
A plant with stunted root growth may have a phosphorus deficiency.
A plant with spindly stalk may have a phosphorus deficiency.
A plant that is purplish in color may have a phosphorus deficiency.
A plant that has delayed in maturing may have a phosphorus deficiency.
A plant with leaf edges that appear scorched may have a potassium deficiency.
A plant with weakened stems may have a potassium deficiency.
A plant with shriveled seeds or fruits may have a potassium deficiency

EXAMPLES:
The plant has stunted root growth.
The plant is purplish in color.
The plant is purplish in color and has delayed in maturing.
'''

# в фактах содержатся пары симптом-вывод
global facts
global is_changed

is_changed = True
facts = [
    ["stunted growth", "nitrogen deficiency"],
    ["pale yellow in color", "nitrogen deficiency"],
    ["reddish-brown leaf edges", "nitrogen deficiency"],
    ["stunted root growth", "phosphorus deficiency"],
    ["spindly stalk", "phosphorus deficiency"],
    ["purplish in color", "phosphorus deficiency"],
    ["delayed in maturing", "phosphorus deficiency"],
    ["leaf edges that appear scorched", "potassium deficiency"],
    ["weakened stems", "potassium deficiency"],
    ["shriveled seeds or fruits", "potassium deficiency"],
    ["green", "balanced nutrition"]
]


# добавляет новый факт
def assert_fact(condition, new_fact):
    global facts
    global is_changed
    if condition and not is_changed and new_fact not in facts:
        facts += [new_fact]
        is_changed = True


# возвращает последний элемент списка
def get_last_element(user_list):
    return user_list[-1]


# возвращает первый элемент списка
def get_first_element(user_list):
    return user_list[0]


while is_changed:
    is_changed = False
    for fact in facts:
        assert_fact(fact[0] == "stunted growth",
                    ["stunted root growth", fact[1]])
print(facts)

if __name__ == '__main__':
    while True:
        # выводы, сделанные на основе фактов
        conclusion = []

        # факт, который вводит пользователь
        user_fact = str(input("\nTell me a fact\n"))

        # проверяем содержит ли факт пользователя известные нашей базе факты
        for fact in facts:
            if user_fact.__contains__(fact[0]) and not conclusion.__contains__(fact[1]):
                conclusion.append(fact[1])

        # если несколько фактов совпало с вводом пользователя, то перечисляем все возможные выводы
        if len(conclusion) >= 1:
            print("This plant may have a", end=' ')

            # избавляемся от взаимоисключающих вариантов
            if conclusion.__contains__("balanced nutrition") and len(conclusion) > 1:
                conclusion.remove("balanced nutrition")

            # составляем конечный вывод
            for conclusion_part in conclusion:
                print(conclusion_part, end=" ")
                if conclusion_part != get_last_element(conclusion):
                    print("and/or", end=" ")

        # если у нас нет информации о фактах пользователя, то выводим соответствующее сообщение
        else:
            print("I don't have enough information")

        conclusion.clear()
