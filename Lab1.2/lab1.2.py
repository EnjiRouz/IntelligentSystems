"""
TASK:
В качестве входных данных для программы должны использоваться факты,
указывающие желательную характеристику, которую должен иметь кустарник,
а результатом работы программы должен быть список растений,
обладающий всеми необходимыми характеристиками.

EXAMPLES:
устойчивость к холоду, простота культивирования, быстрота роста
устойчивость к холоду, устойчивость к затенению, устойчивость к засухе,
устойчивость к влажной почве, устойчивость к кислой почве, устойчивость к городским условиям,
пригодность для кадочного выращивания, простота культивирования, быстрота роста
"""
import xlrd

# открываем файл
database = xlrd.open_workbook('database1.2.xls', formatting_info=True)

# выбираем активный лист
sheet = database.sheet_by_index(0)

# получаем список значений из всех записей и преобразуем его в словарь
plants_characteristics = []
for characteristic_group in [sheet.row_values(i)[1] for i in range(sheet.nrows - 1) if sheet.row_values(i)[1]]:
    plants_characteristics.append(characteristic_group.split(", "))

# в фактах содержатся пары кустарник-характеристики
facts = dict(zip(sheet.col_values(0, 0, sheet.nrows - 1), plants_characteristics))


# возвращает последний элемент списка
def get_last_element(user_list):
    return user_list[-1]


if __name__ == '__main__':
    while True:
        # выводы, сделанные на основе фактов
        conclusion = []

        # факты, которые вводит пользователь
        user_facts = str(input('\nTell me a fact. Example input:\nпростота культивирования, быстрота роста\n')) \
            .split(", ")

        # список занесённых в базу характеристик
        characteristics = []
        for characteristic_group in facts.values():
            for characteristic in characteristic_group:
                characteristics.append(characteristic)
        characteristics = set(characteristics)

        # удаляем повторяющиеся факты
        for user_fact in user_facts:
            while user_facts.count(user_fact) > 1:
                user_facts.remove(user_fact)

        # проверяем, содержат ли факты пользователя известные нашей базе факты, и удаляем лишние
        existing_facts = []
        for user_fact in user_facts:
            if user_fact in characteristics:
                existing_facts.append(user_fact)
        user_facts = existing_facts

        # проверяем, что существуют объекты со всеми искомыми пользователем характеристиками
        if len(user_facts) >= 1:
            for bush_name in facts:
                characteristic = facts.get(bush_name)
                if set(user_facts).issubset(characteristic):
                    conclusion.append(bush_name)

            # если объекты существуют - выводим их названия
            if len(conclusion) >= 1:
                for conclusion_part in conclusion:
                    print(conclusion_part, end="")
                    if conclusion_part != get_last_element(conclusion):
                        print(", ", end="")

            # в противном случае сообщаем, что совпадений не найдено
            else:
                print("I found nothing :(")

        # если не было введено ни одного факта, который известен базе, то выводим сообщение о данной проблеме
        else:
            print("I have nothing to searching for")

        existing_facts.clear()
        conclusion.clear()
        plants_characteristics.clear()
        characteristics.clear()
