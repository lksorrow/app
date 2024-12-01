class User:
    def __init__(self, username, password, role='user'):
        self.username = username.strip()  
        self.password = password
        self.role = role

    def __repr__(self):
        return f"{self.username} ({self.role})"


class Service:
    """Класс для представления услуги ателье."""
    def __init__(self, name, price, description):
        self.name = name.strip()  
        self.price = price
        self.description = description.strip()

    def __repr__(self):
        return f"{self.name} - {self.price} руб | {self.description}"


class Appointment:
    def __init__(self, user, service):
        self.user = user
        self.service = service

    def __repr__(self):
        return f"Запись: {self.user.username} на услугу {self.service.name}"


class AtelierApplication:
    def __init__(self):
        self.users = []
        self.services = []
        self.appointments = []
        self.current_user = None

        self.add_user('admin', 'adminpass', 'admin')
        self.add_user('client1', 'clientpass1')
        self.add_service(Service('Пошив платья', 5000, 'Индивидуальный пошив платья.'))
        self.add_service(Service('Кройка', 2000, 'Кройка по индивидуальным меркам.'))

    def add_user(self, username, password, role='user'):
 
        if any(u.username == username for u in self.users):
            print("Ошибка: Пользователь с таким именем уже существует.")
        else:
            self.users.append(User(username, password, role))
            print(f"Пользователь '{username}' добавлен с ролью '{role}'.")

    def remove_user(self, username):

        initial_count = len(self.users)
        self.users = list(filter(lambda u: u.username != username, self.users))
        if len(self.users) < initial_count:
            print(f"Пользователь '{username}' удален.")
        else:
            print(f"Пользователь '{username}' не найден.")

    def search_user(self, username):

        user = next(filter(lambda u: u.username == username, self.users), None)
        if user:
            print(f"Найден пользователь: {user}")
        else:
            print("Пользователь не найден.")

    def display_users(self):
    
        print("\nСписок пользователей:")
        if self.users:
            print("\n".join(map(str, self.users)))
        else:
            print("Нет зарегистрированных пользователей.")

    def add_service(self, service):
    
        self.services.append(service)
        print(f"Услуга '{service.name}' добавлена.")

    def remove_service(self, service_name):
    
        initial_count = len(self.services)
        self.services = list(filter(lambda s: s.name != service_name, self.services))
        if len(self.services) < initial_count:
            print(f"Услуга '{service_name}' удалена.")
        else:
            print(f"Услуга '{service_name}' не найдена.")

    def search_service(self, service_name):

        service = next(filter(lambda s: s.name == service_name, self.services), None)
        if service:
            print(f"Найдена услуга: {service}")
        else:
            print("Услуга не найдена.")

    def display_services(self):
   
        print("\nСписок услуг:")
        if self.services:
            print("\n".join(map(str, self.services)))
        else:
            print("Нет доступных услуг.")

    def view_appointments(self):
     
        print("\nВаши записи:")
        if self.appointments:
            print("\n".join(map(str, self.appointments)))
        else:
            print("У вас нет записей.")

    def login(self, username, password):
   
        user = next(filter(lambda u: u.username == username and u.password == password, self.users), None)
        if user:
            self.current_user = user
            print(f"Добро пожаловать, {user.username}! Вы вошли как {user.role}.")
        else:
            print("Неверное имя пользователя или пароль.")

    def main_menu(self):
      
        while True:
            print("\nВыберите действие:")
            print("1. Авторизация")
            print("2. Выход")
            choice = input("Ваш выбор: ")
            
            if choice == '1':
                username = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")
                self.login(username, password)
                self.user_menu()
            elif choice == '2':
                print("Вы вышли из приложения.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def user_menu(self):
        while self.current_user:
            if self.current_user.role == "user":
                print("\n1. Посмотреть услуги")
                print("2. Записаться на услугу")
                print("3. Просмотр своих записей")
                print("4. Назад")

                user_choice = input("Ваш выбор: ")
                if user_choice == '1':
                    self.display_services()
                elif user_choice == '2':
                    service_index = int(input("Введите номер услуги для записи: ")) - 1
                    if 0 <= service_index < len(self.services):
                        self.appointments.append(Appointment(self.current_user, self.services[service_index]))
                        print(f"Вы записались на услугу: {self.services[service_index].name}")
                    else:
                        print("Ошибка: Неверный номер услуги.")
                elif user_choice == '3':
                    self.view_appointments()
                elif user_choice == '4':
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")
            else:
                print("\nВы находитесь в меню администратора.")
                print("1. Управление пользователями")
                print("2. Управление услугами")
                print("3. Выход")

                admin_choice = input("Ваш выбор: ")
                if admin_choice == '1':
                    self.admin_user_menu()
                elif admin_choice == '2':
                    self.admin_service_menu()
                elif admin_choice == '3':
                    self.current_user = None  
                else:
                    print("Неверный выбор. Попробуйте снова.")

    def admin_user_menu(self):

        while True:
            print("\n1. Добавить пользователя")
            print("2. Удалить пользователя")
            print("3. Поиск пользователя")
            print("4. Список пользователей")
            print("5. Назад")
            admin_user_choice = input("Ваш выбор: ")

            if admin_user_choice == '1':
                username = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")
                role = input("Введите роль (user/admin): ")
                self.add_user(username, password, role)
            elif admin_user_choice == '2':
                username = input("Введите имя пользователя для удаления: ")
                self.remove_user(username)
            elif admin_user_choice == '3':
                username = input("Введите имя пользователя для поиска: ")
                self.search_user(username)
            elif admin_user_choice == '4':
                self.display_users()
            elif admin_user_choice == '5':
                break
            else:
                print("Неверный выбор.")


    def admin_service_menu(self):

        while True:
            print("\n1. Добавить услугу")
            print("2. Удалить услугу")
            print("3. Поиск услуги")
            print("4. Список услуг")
            print("5. Назад")
            admin_service_choice = input("Ваш выбор: ")

            if admin_service_choice == '1':
                name = input("Введите имя услуги: ")
                price = float(input("Введите цену услуги: "))
                description = input("Введите описание услуги: ")
                self.add_service(Service(name, price, description))
            elif admin_service_choice == '2':
                service_name = input("Введите имя услуги для удаления: ")
                self.remove_service(service_name)
            elif admin_service_choice == '3':
                service_name = input("Введите имя услуги для поиска: ")
                self.search_service(service_name)
            elif admin_service_choice == '4':
                self.display_services()
            elif admin_service_choice == '5':
                break
            else:
                print("Неверный выбор.")


if __name__ == "__main__":
    app = AtelierApplication()
    app.main_menu()