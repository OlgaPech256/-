from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, max_speed):
        # Валидация аргументов конструктора
        if not isinstance(brand, str) or not brand:
            raise ValueError("Марка должна быть непустой строкой.")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом.")

        self.brand = brand
        self.max_speed = max_speed

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return f"Машина {self.brand} движется со скоростью {self.max_speed} км/ч."

class Bicycle(Vehicle):
    def drive(self):
        return f"Велосипед {self.brand} движется со скоростью {self.max_speed} км/ч."

    from abc import ABC, abstractmethod

    class Appliance(ABC):
        def __init__(self, power_usage, brand):
            # Валидация аргументов конструктора
            if not isinstance(power_usage, (int, float)) or power_usage <= 0:
                raise ValueError("Потребление электроэнергии должно быть положительным числом.")
            if not isinstance(brand, str) or not brand:
                raise ValueError("Марка должна быть непустой строкой.")

            self.power_usage = power_usage
            self.brand = brand

        @abstractmethod
        def turn_on(self):
            pass

    class WashingMachine(Appliance):
        def turn_on(self):
            return f"Стиральная машина {self.brand} включена, потребляемая мощность {self.power_usage} Вт."

    class Refrigerator(Appliance):
        def turn_on(self):
            return f"Холодильник {self.brand} включен, потребляемая мощность {self.power_usage} Вт."

        from abc import ABC, abstractmethod

        class Animal(ABC):
            def __init__(self, species, age):
                # Валидация аргументов конструктора
                if not isinstance(species, str) or not species:
                    raise ValueError("Вид должен быть непустой строкой.")
                if not isinstance(age, (int, float)) or age < 0:
                    raise ValueError("Возраст должен быть неотрицательным числом.")

                self.species = species
                self.age = age

            @abstractmethod
            def make_sound(self):
                pass

        class Dog(Animal):
            def make_sound(self):
                return "Собака лает."

        class Cat(Animal):
            def make_sound(self):
                return "Кошка мяукает."