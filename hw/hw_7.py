import sqlite3

connect = sqlite3.connect('phones.db')

cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS phones (
            name VARCHAR(50) NOT NULL,
            year INTEGER NOT NULL,
            cpu VARCHAR(20),
            memory INTEGER
        )
''')
connect.commit()

def create_phone(name, year, cpu=None, memory=None):
    cursor.execute(
        'INSERT INTO phones (name, year, cpu, memory) VALUES (?, ?, ?, ?)',
        (name, year, cpu, memory)
    )
    connect.commit()
    print(f'телефон добавлен {name}!!')

# create_phone('Iphone 11 pro', 2019, 'A13 bionic', 256)
# create_phone('Iphone 12 pro', 2020)
# create_phone('samsung s21', 2021, 'snapdragon 888', 512)
# create_phone('Iphone 17 promax', 2024,None,  1024)

def get_info():
    cursor.execute('SELECT * FROM phones')
    phones = cursor.fetchall()
    for i in phones:
        print(f"NAME: {i[0]} YEAR: {i[1]} CPU: {i[2]}, MEMORY: {i[3]}")

get_info()


def update_memory(row_id, memory):
    cursor.execute(
        'UPDATE phones SET memory = ? WHERE rowid = ?',
        (memory, row_id)
    )
    connect.commit()
    print('Измениния добавлены')

update_memory(3, 128)

def delete_phone(row_id):
    cursor.execute(
        'DELETE FROM phones WHERE rowid = ?',
        (row_id,)
    )
    connect.commit()
    print('Телефон удален!!')

delete_phone(1)

def get_phone(row_id):
    cursor.execute('SELECT * FROM phones WHERE rowid = ?', (row_id,))
    phone = cursor.fetchone()
    if phone:
        print(f"NAME: {phone[0]} YEAR: {phone[1]} CPU: {phone[2]}, MEMORY: {phone[3]}")
    else:
        print('Телефон не найден')

get_phone(4)