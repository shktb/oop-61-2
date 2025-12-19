"""Faker Python это библиотека Python для генерации реалистичных, но вымышленных данных.
С помощью библиотеки faker мы можем создавать выдуманные данные на английском и русском языке.
В этом примере мы создаем лист с данными несуществующих людей"""



from  faker import Faker

fake = Faker("ru_RU")

users = []

for _ in range(3):
    users.append({
        "name": fake.name(),
        "email": fake.email(),
        "birth day": fake.date_of_birth(),
    })

for dictionary in users:
    print(dictionary)
