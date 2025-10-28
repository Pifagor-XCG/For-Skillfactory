import random
from operator import index
from types import new_class

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удаление ученика
        5. Удаление предмета
        6. Удаление оценок
        7. Редактировать ученика
        8. Редактировать предмет
        9. Редактировать оценку
        10. Вывод информации по всем оценкам для определенного ученика.
        11. Вывод среднего балла по каждому предмету по определенному ученику.
        12. Добавить новый предмет 
        13. Выход из программы
        ''')


while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        print("4. Удалить ученика")
        student = input('Введите имя ученика для удаления: ')

        if student in students_marks:
            del students_marks[student]
            print(f"Ученик {student} был удален")
            print("Список учеников")
            for student in students_marks:
                print(f"\t{student}")
        else:
            print("Такого ученика не существует")
    elif command == 5:
        print("Удалить предмет")
        predmet = input("Введите предмет который желаете удалить: ")
        predmet_nashli = False
        for student in students_marks:
            if predmet in students_marks[student]:
                del students_marks[student][predmet]
                predmet_nashli = True
        if predmet_nashli:
            classes.remove(predmet)
            print(f"Предмет {predmet} был удален")
            print("Список предметов")
            print(f"\t{classes}")
        else:
            print("Такого предмета не существует")
        print()
    elif command == 6:
        print("Удалить оценки")
        for student in students_marks:
            for marks in students_marks[student]:
                students_marks[student][marks].clear()
        for key, value in students_marks.items():
            print(f"\t{key} - {value}")
        print()
    elif command == 7:
        print("Изменить имя ученика")
        staroe_name = input("Введите имя которое желаете изменить: ")
        if staroe_name in students_marks:
            name = input("Введите имя на которое желаете изменить: ")
            students_marks[name] = students_marks.pop(staroe_name)
            print(f"Имя {staroe_name} изменено на {name}")
            print("Список учеников")
            for key in students_marks:
                print(f"\t{key}")
        else:
            print("Такого имени нет в списке")
        print()
    elif command == 8:
        print("Изменить предмет")
        stariy_class = input("Введите предмет который желаете изменить: ")
        new_class = input("Введите предмет на который желаете изменить: ")
        predmet_nashli = False
        for student in students_marks:
            if stariy_class in students_marks[student]:
                students_marks[student][new_class] = students_marks[student].pop(stariy_class)
                predmet_nashli = True
        if predmet_nashli:
            print(f"Предмет {stariy_class} изменен на {new_class}")
            print("Список учеников")
            print(f"\t{students_marks}")
        else:
            print("Такого предмета нет в списке")
        print()
    elif command == 9:
        print("Изменить оценку")
        name = input("Введите ученика у которого желаете изменить оценку: ")
        if name in students_marks:
            predmet = input("Введите предмет у которого желаете изменить оценку: ")
            if predmet in students_marks[name]:
                marks = students_marks[name][predmet]
                if marks:
                    print(f"Оценки у {name} по {predmet} данный момент")
                    print(f"\t{students_marks[name][predmet]}")
                    index_ = int(input(f"Введите номер оценки (0-{len(marks) - 1}): "))
                    new_ocenka = int(input("Введите новую оценку: "))
                    marks[index_] = new_ocenka
                    print(f"Оценка у {name} по предмету {predmet} изменена на {new_ocenka}")
                    print(f"Оценки у {name} на данный момент")
                    print(f"\t{students_marks[name]}")

            else:
                print("Такого предмета нет в списке")
        else:
            print("Такого ученика нет в списке")
        print()
    elif command == 10:
        print("Информация по всем оценкам для определенного ученика")
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f"Оценки ученика:{student}")
            for value, key in students_marks[student].items():
                print(f"\t{value} - {key}")
        else:
            print("Такого ученика нет в списке")

            print()
    elif command == 11:
        print("Вывод среднего балла по каждому предмету")
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(student)
            for class_ in classes:
                if class_ in students_marks[student]:
                    marks_sum = sum(students_marks[student][class_])
                    marks_count = len(students_marks[student][class_])
                    if marks_count > 0:
                        print(f'{class_} - {marks_sum // marks_count}')
                else:
                    print("Такого ученика нет в списке")
        else:
            print("Такого ученика нет в списке")
            print()
    elif command == 12:
        new_class = input("Введите название предмета который желаете добавить: ")
        if new_class not in classes:
            classes.append(new_class)
            print(f"Добавлен новый предмет - {new_class}")
            print("Список предметов")
            print(f"\t{classes}")
        else:
            print("Данный предмет уже существует")

        print()
    elif command == 13:
        print("Вы вышли из программы")
        break