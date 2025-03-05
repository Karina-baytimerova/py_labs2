# Базовый класс для операционных систем
class OperatingSystem:

    def __init__(self, name: str, version: str, release_year: int) -> None:
        self.name = name  # Название ОС
        self.version = version  # Версия ОС
        self.release_year = release_year  # Год выпуска

    def __str__(self) -> str:
        return f"{self.name} {self.version} ({self.release_year})"

    def __repr__(self) -> str:
        return f"OperatingSystem(name={self.name!r}, version={self.version!r}, release_year={self.release_year!r})"

    def get_info(self) -> str:
        return f"OS: {self.name}, Version: {self.version}, Released: {self.release_year}"


# Дочерний класс для MacOS
class MacOS(OperatingSystem):

    def __init__(self, name: str, version: str, release_year: int, apple_silicon: bool = False) -> None:
        super().__init__(name, version, release_year)  # Вызов конструктора родительского класса
        self.apple_silicon = apple_silicon  # Поддержка Apple Silicon

    def __str__(self) -> str:
        base_info = super().__str__()  # Используем метод родительского класса
        return f"{base_info}, Apple Silicon: {'Yes' if self.apple_silicon else 'No'}"

    def __repr__(self) -> str:
        return f"MacOS(name={self.name!r}, version={self.version!r}, release_year={self.release_year!r}, apple_silicon={self.apple_silicon!r})"

    def get_info(self) -> str:
        base_info = super().get_info()  # Используем метод родительского класса
        return f"{base_info}, Apple Silicon Support: {'Yes' if self.apple_silicon else 'No'}"

    def check_compatibility(self, device_type: str) -> bool:
        if device_type.lower() == "apple silicon":
            return self.apple_silicon  # Возвращает True, если поддерживается Apple Silicon
        return True  # Для всех других устройств совместимость есть


# Пример использования
if name == "__main__":
    # Создаем объект базового класса
    os_base = OperatingSystem("Linux", "5.15", 2021)
    print(os_base)  # Выводит: Linux 5.15 (2021)
    print(repr(os_base))  # Выводит: OperatingSystem(name='Linux', version='5.15', release_year=2021)
    print(os_base.get_info())  # Выводит: OS: Linux, Version: 5.15, Released: 2021

    # Создаем объект дочернего класса
    os_mac = MacOS("MacOS", "Monterey", 2021, True)
    print(os_mac)  # Выводит: MacOS Monterey (2021), Apple Silicon: Yes
    print(repr(os_mac))  # Выводит: MacOS(name='MacOS', version='Monterey', release_year=2021, apple_silicon=True)
    print(os_mac.get_info())  # Выводит: OS: MacOS, Version: Monterey, Released: 2021, Apple Silicon Support: Yes
    print(os_mac.check_compatibility("Apple Silicon"))  # Выводит: True

