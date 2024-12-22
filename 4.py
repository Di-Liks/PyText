import os
import getpass
import base64

def generate_password(length=16):
    return base64.b64encode(os.urandom(length)).decode('utf-8')

def main():
    allowed_username = "name"

    current_username = getpass.getuser()

    if current_username == allowed_username:
        print(f"Добро пожаловать, {current_username}!")
        password = generate_password()
        print(f"Сгенерированный пароль: {password}")
    else:
        print("Доступ запрещен. Эта программа предназначена для другого пользователя.")

if __name__ == "__main__":
    main()
