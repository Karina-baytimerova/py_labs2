import doctest

class User:
    def __init__(self, name: str, age: int, email: str):
        """
        Создание и подготовка к работе объекта "Пользователь"

        :param name: Имя пользователя
        :param age: Возраст пользователя
        :param email: Электронная почта пользователя

        Примеры:
        >>> user = User("Иван", 25, "ivan@example.com")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if not isinstance(email, str):
            raise TypeError("Электронная почта должна быть строкой")
        if "@" not in email:
            raise ValueError("Электронная почта должна содержать символ '@'")

        self.name = name
        self.age = age
        self.email = email

    def is_adult(self) -> bool:
        """
        Проверка, является ли пользователь совершеннолетним.

        :return: True, если пользователь совершеннолетний, иначе False

        Примеры:
        >>> user = User("Иван", 25, "ivan@example.com")
        >>> user.is_adult()
        True
        """
        return self.age >= 18

    def update_email(self, new_email: str) -> None:
        """
        Обновление электронной почты пользователя.

        :param new_email: Новая электронная почта
        :raise ValueError: Если новая электронная почта не содержит символ '@'

        Примеры:
        >>> user = User("Иван", 25, "ivan@example.com")
        >>> user.update_email("ivan_new@example.com")
        """
        if not isinstance(new_email, str):
            raise TypeError("Электронная почта должна быть строкой")
        if "@" not in new_email:
            raise ValueError("Электронная почта должна содержать символ '@'")
        self.email = new_email


class Car:
    def __init__(self, brand: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом")
        if year < 1886:  # Первый автомобиль был создан в 1886 году
            raise ValueError("Год выпуска не может быть раньше 1886")

        self.brand = brand
        self.model = model
        self.year = year

    def get_age(self, current_year: int = 2025) -> int:
        """
        Возвращает возраст автомобиля.

        :param current_year: Текущий год (по умолчанию 2025)
        :return: Возраст автомобиля

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.get_age()
        5
        """
        if not isinstance(current_year, int):
            raise TypeError("Текущий год должен быть целым числом")
        if current_year < self.year:
            raise ValueError("Текущий год не может быть меньше года выпуска автомобиля")
        return current_year - self.year

    def update_model(self, new_model: str) -> None:
        """
        Обновление модели автомобиля.

        :param new_model: Новая модель автомобиля

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.update_model("Camry")
        """
        if not isinstance(new_model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        self.model = new_model


class City:
    def __init__(self, name: str, population: int, country: str):
        """
        Создание и подготовка к работе объекта "Город"

        :param name: Название города

Карина, [03.03.2025 22:53]
:param population: Население города
        :param country: Страна, в которой находится город

        Примеры:
        >>> city = City("Москва", 12000000, "Россия")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название города должно быть строкой")
        if not isinstance(population, int):
            raise TypeError("Население города должно быть целым числом")
        if population < 0:
            raise ValueError("Население города не может быть отрицательным")
        if not isinstance(country, str):
            raise TypeError("Страна должна быть строкой")

        self.name = name
        self.population = population
        self.country = country

    def is_megacity(self, threshold: int = 1000000) -> bool:
        """
        Проверка, является ли город мегаполисом.

        :param threshold: Порог населения для мегаполиса (по умолчанию 1,000,000)
        :return: True, если город является мегаполисом, иначе False

        Примеры:
        >>> city = City("Москва", 12000000, "Россия")
        >>> city.is_megacity()
        True
        """
        if not isinstance(threshold, int):
            raise TypeError("Порог населения должен быть целым числом")
        if threshold < 0:
            raise ValueError("Порог населения не может быть отрицательным")
        return self.population >= threshold

    def update_population(self, new_population: int) -> None:
        """
        Обновление населения города.

        :param new_population: Новое население города
        :raise ValueError: Если новое население отрицательное

        Примеры:
        >>> city = City("Москва", 12000000, "Россия")
        >>> city.update_population(13000000)
        """
        if not isinstance(new_population, int):
            raise TypeError("Население города должно быть целым числом")
        if new_population < 0:
            raise ValueError("Население города не может быть отрицательным")
        self.population = new_population


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
