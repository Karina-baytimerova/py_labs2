# Базовый класс для операционных систем
class OperatingSystem:

    def __init__(self, name: str, version: str, release_year: int) -> None:
        self.name = name  # Название ОС
        self.version = version  # Версия ОС
        self.release_year = release_year  # Год выпуска

    def __str__(self) -> str:
        return f"{self.name} {self.version} ({self.release_year})"

    def __repr__(self) -> str:
        return f"OperatingSystem(name='{self.name}', version='{self.version}', release_year={self.release_year})"

    def get_info(self) -> str:
        return f"OS: {self.name}, Version: {self.version}, Released: {self.release_year}"


# Дочерний класс для MacOS

class MacOS(OperatingSystem):
    
    def __init__(self, name: str, version: str, release_year: int, apple_silicon: bool = False) -> None:
        super().__init__(name, version, release_year)  # Наследуем конструктор базового класса
        self.apple_silicon = apple_silicon  # Поддержка Apple Silicon

    def __repr__(self) -> str:
        # Перегружаем __repr__
        return (f"MacOS(name='{self.name}', version='{self.version}', "
                f"release_year={self.release_year}, apple_silicon={self.apple_silicon})")

    def __str__(self) -> str:
        # str перегружзн
        base_info = super().__str__()
        return f"{base_info}, Apple Silicon: {'Yes' if self.apple_silicon else 'No'}"

    # Метод get_info унаследован

    def check_compatibility(self, device_type: str) -> bool:
        # Перегружаем метод, чтобы добавить проверку совместимости
        if device_type.lower() in ["macbook", "imac", "mac mini"]:
            return True
        if self.apple_silicon and device_type.lower() == "ipad":
            return True
        return False



# Пример использования
if __name__ == "__main__":
    os_mac = MacOS("MacOS", "Ventura", 2023, True)
    
    # __repr__ перегружен — отображает все параметры, включая apple_silicon
    print(repr(os_mac))  # Output: MacOS(name='MacOS', version='Ventura', release_year=2023, apple_silicon=True)

    # __str__ перегружен
    print(os_mac)  # Output: MacOS Ventura (2023), Apple Silicon: Yes

    # Метод get_info унаследован
    print(os_mac.get_info())  # Output: OS: MacOS, Version: Ventura, Released: 2023

    # Проверка совместимости
    print(os_mac.check_compatibility("iPad"))  # True

