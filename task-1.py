from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @property
    @abstractmethod
    def spec(self):
        return ""

    def model_with_spec(self, model) -> str:
        return f"{model} ({self.spec})"

    def create_car(self, make, model) -> Car:
        return Car(make, self.model_with_spec(model))

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, self.model_with_spec(model))


class USVehicleFactory(VehicleFactory):
    @property
    def spec(self):
        return "US Spec"


class EUVehicleFactory(VehicleFactory):
    @property
    def spec(self):
        return "EU Spec"


# Використання
us_factory: VehicleFactory = USVehicleFactory()
eu_factory: VehicleFactory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Toyota", "Corolla")
vehicle1.start_engine()


vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
