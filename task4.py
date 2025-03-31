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


# Дочерний класс для MacOS (наследует метод __repr__ без изменений)
class MacOS(OperatingSystem):

    def __init__(self, name: str, version: str, release_year: int, apple_silicon: bool = False) -> None:
        super().__init__(name, version, release_year)  # Вызов конструктора родителя
        self.apple_silicon = apple_silicon  # Поддержка Apple Silicon

    def __str__(self) -> str:
        base_info = super().__str__()  # Используем родительский __str__
        return f"{base_info}, Apple Silicon: {'Yes' if self.apple_silicon else 'No'}"

    # Метод __repr__ не перегружен — наследуется из OperatingSystem

    def get_info(self) -> str:
        base_info = super().get_info()  # Используем родительский get_info
        return f"{base_info}, Apple Silicon Support: {'Yes' if self.apple_silicon else 'No'}"

    def check_compatibility(self, device_type: str) -> bool:
        if device_type.lower() == "apple silicon":
            return self.apple_silicon
        return True


# Пример использования
if __name__ == "__main__":
    os_mac = MacOS("MacOS", "Ventura", 2023, True)
    
    # __repr__ унаследован из OperatingSystem (не содержит apple_silicon)
    print(repr(os_mac))  # Output: OperatingSystem(name='MacOS', version='Ventura', release_year=2023)

    # Остальные методы работают как раньше
    print(os_mac)  # Output: MacOS Ventura (2023), Apple Silicon: Yes
    print(os_mac.get_info())  # Output: OS: MacOS, Version: Ventura, Released: 2023, Apple Silicon Support: Yes

