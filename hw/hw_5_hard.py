class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
allowed_comands = {
    "admin": ["start", "ban", "stop"],
    "user": ["start", "message"]
}

def verification(command_name):
    def decorator(func):
        def wrapper(self, user: User):
            if command_name not in allowed_comands.get(user.role, []):
                print(f'Пользователь {user.username} ({user.role}) не может выполнять команду "{command_name}"')
            else:
                print(f'Пользователь {user.username} ({user.role}) выполняет команду {command_name}')
                return func(self, user)

        return wrapper
    return decorator

class CommandHandler:

    @verification("start")
    def start(self, user):
        print("Команда start выполнена")

    @verification("ban")
    def ban(self, user):
        print("Команда ban выполнена")

    @verification("stop")
    def stop(self, user):
        print("Команда stop выполнена")

    @verification("message")
    def message(self, user):
        print(f"Пользователь {user.username} отправил сообщение")

user1 = User("Alice", "admin")
user2 = User("Bob", "user")

handler = CommandHandler()

handler.start(user1)
handler.ban(user1)
handler.stop(user1)
handler.message(user1)

handler.start(user2)
handler.ban(user2)
handler.message(user2)

