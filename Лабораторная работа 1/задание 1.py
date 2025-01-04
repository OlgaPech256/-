from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def capacity(self):
        pass

class Car(Transport):
    def move(self):
        return "Car is driving"

    def fuel_type(self):
        return "Gasoline"

    def capacity(self):
        return 5  # number of passengers

class Bicycle(Transport):
    def move(self):
        return "Bicycle is pedaling"

    def fuel_type(self):
        return "Human power"

    def capacity(self):
        return 1  # number of passengers

    from abc import ABC, abstractmethod

    class Appliance(ABC):
        @abstractmethod
        def turn_on(self):
            pass

        @abstractmethod
        def turn_off(self):
            pass

        @abstractmethod
        def get_power_usage(self):
            pass

    class WashingMachine(Appliance):
        def turn_on(self):
            return "Washing Machine is now ON"

        def turn_off(self):
            return "Washing Machine is now OFF"

        def get_power_usage(self):
            return "2000 Watts"

    class Refrigerator(Appliance):
        def turn_on(self):
            return "Refrigerator is now ON"

        def turn_off(self):
            return "Refrigerator is now OFF"

        def get_power_usage(self):
            return "150 Watts"

        from abc import ABC, abstractmethod

        class Media(ABC):
            @abstractmethod
            def play(self):
                pass

            @abstractmethod
            def pause(self):
                pass

            @abstractmethod
            def stop(self):
                pass

        class Music(Media):
            def play(self):
                return "Playing music"

            def pause(self):
                return "Pausing music"

            def stop(self):
                return "Stopping music"

        class Video(Media):
            def play(self):
                return "Playing video"

            def pause(self):
                return "Pausing video"

            def stop(self):
                return "Stopping video"