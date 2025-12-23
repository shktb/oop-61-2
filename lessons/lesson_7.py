import sqlite3

# A4
connect = sqlite3.connect('users.db')
# рука с корандашом
cursor = connect.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS (
            name VARCHAR (50) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')
connect.commit()


#  CRUD - Create Read Update Delete

def create_user(name, age, hobby=None):
    # cursor.execute(
    #     f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")'
    # )
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f'пользователь добавлен {name}!!')

# create_user("Slava", 33, "кодить!!")


def get_users():
    cursor.execute('SELECT name, hobby, age FROM users')
    users = cursor.fetchmany(3)
    # print(users)
    for i in users:
        print(f"NAME: {i[0]} AGE: {i[1]} HOBBY: {i[2]}")

# get_users()


def update_user_name(row_id, name):
    cursor.execute(
        'UPDATE users SET hobby = ? WHERE rowid = ?',
        (name, row_id)
    )
    connect.commit()
    print('пользователь обнавлен!')

update_user_name(3, 'Любит горы летом!!')

def delete_user(row_id):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (row_id,)
    )
    connect.commit()
    print('Пользователь удален!!')


# delete_user(2)

