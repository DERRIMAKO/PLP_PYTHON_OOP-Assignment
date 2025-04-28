# Object-Oriented Programming
# Assignment Title: Design Your Own Class!

# Define a Smartphone class using encapsulation and inheritance
class Smartphone:
    """Represents a smartphone with private attributes and controlled access."""

    def __init__(self, brand, model, storage):
        self.__brand = brand  # Private attribute
        self.__model = model
        self.__storage = storage

    # Getter and Setter methods for controlled access
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def display_info(self):
        """Returns smartphone details."""
        return f"{self.__brand} {self.__model}, Storage: {self.__storage}GB"

# Subclass for GamingSmartphones (Inheritance)
class GamingSmartphone(Smartphone):
    """Represents a gaming smartphone with additional features."""

    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.__cooling_system = cooling_system

    def display_info(self):
        """Polymorphic method: Displays gaming smartphone details."""
        return f"{self.get_brand()} {self.__model}, Storage: {self.__storage}GB, Cooling: {self.__cooling_system}"

# Demonstrate encapsulation and inheritance
phone = Smartphone("Samsung", "Galaxy S23", 256)
gaming_phone = GamingSmartphone("ASUS", "ROG Phone 7", 512, "Liquid Cooling")

print(phone.display_info())
print(gaming_phone.display_info())
