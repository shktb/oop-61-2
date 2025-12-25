import sqlite3

connect = sqlite3.connect('statement.db')
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL
            )
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson TEXT,
        grade INTEGER,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')
connect.commit()

def create_user(name):
    cursor.execute('INSERT INTO users(name) VALUES (?)', (name,))
    connect.commit()
    print(f'Пользователь создан {name}!')

def create_grade(user_id, lesson, grade):
    cursor.execute('INSERT INTO grades(user_id, lesson, grade) VALUES (?, ?, ?)'
                    , (user_id, lesson, grade))
    connect.commit()
    print(f'Оценка по "{lesson}" выставлена')

def get_users_grades():
    cursor.execute("""
    SELECT users.name, grades.lesson, grades.grade
    FROM users
    LEFT JOIN grades ON users.id = grades.user_id
    """)

    rows = cursor.fetchall()
    for i in rows:
        print(f"Имя: {i[0]} | Предмет: {i[1]} | Оценка: {i[2]}")


def grades_statistics():
    cursor.execute("""
        SELECT
            COUNT(grade),
            MAX(grade),
            MIN(grade),
            AVG(grade)
        FROM grades
        """)
    count, max_g, min_g, avg_g = cursor.fetchone()
    print(f"""
        Количество оценок: {count}
        Максимальная: {max_g}
        Минимальная: {min_g}
        Средняя: {round(avg_g, 2)}
        """)


def grades_count_per_user():
    cursor.execute("""
    SELECT users.name, COUNT(grades.id)
    FROM users
    LEFT JOIN grades ON users.id = grades.user_id
    GROUP BY users.id
    """)

    for name, count in cursor.fetchall():
        print(f"{name} — {count} оценок")


def students_with_high_grades(min_grade):
    cursor.execute("""
    SELECT name FROM users
    WHERE id IN (
        SELECT user_id FROM grades
        WHERE grade >= ?
    )
    """, (min_grade,))

    for (name,) in cursor.fetchall():
        print(name)


def create_view():
    cursor.execute("""
            CREATE VIEW IF NOT EXISTS user_grades_view AS
            SELECT 
                users.name, 
                grades.lesson, 
                grades.grade
            FROM users
            LEFT JOIN grades ON users.id = grades.user_id
        """)
    connect.commit()

def show_view():
    cursor.execute("SELECT * FROM user_grades_view")
    for row in cursor.fetchall():
        print(row)

create_user("Аня")
create_user("Илья")
create_user("Диана")

create_grade(1, "Математика", 5)
create_grade(1, "Физика", 4)
create_grade(2, "Математика", 3)
create_grade(4, "Математика", 5)

get_users_grades()
grades_statistics()
grades_count_per_user()
students_with_high_grades(4)
create_view()
show_view()