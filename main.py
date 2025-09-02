class PasswordManager:
    def __init__(self, master_key: str):
        self.master_key = master_key
        self.passwords = {}

    def check_master_password(self) -> bool:
        count = 0
        while count < 3:
            try:
                user_key = input('Введите мастер-пароль: ')
            except KeyboardInterrupt:
                print('\nВвод прерван.')
                return False
            if user_key != self.master_key:
                count += 1
                print(
                    f'Не правильный пароль, у вас осталось {3 - count} попытки\n')
            else:
                return True
        return False

    def menu(self):
        while True:
            print(f'\n1. Добавить пароль')
            print(f'2. Показать пароли')
            print(f'3. Удалить пароль')
            print(f'4. Выход из программы')
            try:
                user_choice = int(input('Ваш выбор: '))
            except ValueError:
                print("\nПожалуйста, введите число от 1 до 4.")
                continue
            except KeyboardInterrupt:
                print('\nВвод прерван.')
                return False

            if user_choice == 1:
                self.add_password()
            elif user_choice == 2:
                self.show_password()
            elif user_choice == 3:
                self.delete_password()
            elif user_choice == 4:
                print("BYE BYE")
                break

    def add_password(self):
        service = input('\nВведи имя сервиса/сайта: ')
        account = input('Введи имя аккаунта: ')
        password = input('Введите пароль: ')

        if service in self.passwords:
            print('\nСервис {service} уже существует.')
            user_choice = input("Хотите заменить(1) или добавить новый(2)? ")

            if user_choice == '1':
                self.passwords[service] = {
                    "account": account, "password": password}
                print("\nПароль успешно обновлён!")
                return

            elif user_choice == '2':
                index = 2
                while f'{service}({index})' in self.passwords:
                    index += 1
                service = f'{service}({index})'

            else:
                print('\nНекорректный ввод. Отмена')
                return

        self.passwords[service] = {
            "account": account, "password": password}
        print(f'\nСервис "{service}" добавлен.')

    def show_password(self):
        print(self.passwords)

    def delete_password(self):
        all_keys = list(self.passwords.keys())
        print('Какой сервис вы хотите удалить?')
        print(*all_keys, sep='\n')


manager = PasswordManager(master_key='abs')
if manager.check_master_password():
    print("Доступ разрешён")
    manager.menu()
else:
    print("Доступ запрещён")
