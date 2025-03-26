class OperatingSystem:

    def __init__(self, name: str, version: str, release_year: int) -> None:
        self.name = name
        self.version = version
        self.release_year = release_year

    def __str__(self) -> str:
        return f"{self.name} {self.version} ({self.release_year})"

    def __repr__(self) -> str:
        return f"OperatingSystem(name={self.name!r}, version={self.version!r}, release_year={self.release_year!r})"

    def get_info(self) -> str:
        return f"OS: {self.name}, Version: {self.version}, Released: {self.release_year}"


class MacOS(OperatingSystem):

    def __init__(self, name: str, version: str, release_year: int, apple_silicon: bool = False) -> None:
        super().__init__(name, version, release_year)
        self.apple_silicon = apple_silicon

    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info}, Apple Silicon: {'Yes' if self.apple_silicon else 'No'}"

    def __repr__(self) -> str:
        return (f"MacOS(name={self.name!r}, version={self.version!r}, "
                f"release_year={self.release_year!r}, apple_silicon={self.apple_silicon!r})")

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Apple Silicon Support: {'Yes' if self.apple_silicon else 'No'}"

    def check_compatibility(self, device_type: str) -> bool:
        if device_type.lower() == "apple silicon":
            return self.apple_silicon
        return True


if __name__ == "__main__":
    os_base = OperatingSystem("Linux", "5.15", 2021)
    print(os_base)
    print(repr(os_base))
    print(os_base.get_info())

    os_mac = MacOS("MacOS", "Monterey", 2021, True)
    print(os_mac)
    print(repr(os_mac))
    print(os_mac.get_info())
    print(os_mac.check_compatibility("Apple Silicon"))

