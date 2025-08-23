class Superhero:
    def __init__(self, real_name, superhero_name):
        self.__real_name = real_name  # Приватное свойство (скрытое от внешнего доступа)
        self.superhero_name = superhero_name  # Публичное свойство

    # Метод-геттер для доступа к реальному имени (секретной личности)
    def get_real_name(self):
        return self.__real_name

    # Метод-сеттер для изменения реального имени (секретной личности)
    def set_real_name(self, new_real_name):
        if len(new_real_name) > 3:  # Добавляем проверку
            self.__real_name = new_real_name
        else:
            print("Реальное имя должно содержать не менее 4 символов.")

    def reveal_identity(self):
        print(f"Я - {self.superhero_name}, моя настоящая личность - {self.__real_name}.")

# Создаем объект супергероя
halk = Superhero("Брюс Бэннер", "Халк")

# Доступ к публичному свойству
print(halk.superhero_name)

# Попытка доступа к приватному свойству (секретной личности) напрямую вызовет ошибку
# print(halk.__real_name)

# Доступ к приватному свойству с использованием метода-геттера
#### Задание 1. Получи значение приватного свойства объекта halk
print(halk.get_real_name())

#### Задание 2. Изменени реальное имя с использованием метода-сеттера на "Доктор Брюс Бэннер"
halk.set_real_name("12345")
halk.reveal_identity()