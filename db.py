import sqlite3


def create_db():
    conn = sqlite3.connect('students.db')
    curs = conn.cursor()
    curs.execute('''create table if not exists students
                 (id integer primary key autoincrement, name text, grade integer)''')
    conn.commit()
    conn.close()


def add_student():
    name = input("Имя студента: ")
    grade = int(input("Введите оценку студента: "))

    conn = sqlite3.connect('students.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
    conn.commit()
    conn.close()
    print("Оценка добавлена")


def update_grade():
    student_id = int(input("Введите ID студента: "))
    new_grade = int(input("Введите новую оценку: "))

    conn = sqlite3.connect('students.db')
    curs = conn.cursor()
    curs.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    conn.commit()
    conn.close()
    print("Оценка обновлена")


def show_students():
    conn = sqlite3.connect('students.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM students")
    students = curs.fetchall()
    conn.close()
    if students:
        print("Список студентов:")
        for student in students:
            print(f"ID: {student[0]}, Имя: {student[1]}, Оценка: {student[2]}")
    else:
        print("В базе ничего нет(")


create_db()

while True:
    print("\nВыберите действие:")
    print("1. Добавить студента")
    print("2. Обновить оценку")
    print("3. Показать список студентов с оценками")
    print("4. Закончить сеанс")
    choice = input("Введите номер действия: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        show_students()
    elif choice == "4":
        break
    else:
        print("Введите соответствующий номер!!")