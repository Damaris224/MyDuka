class Car:
    def __init__(self, brand, model, year, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0
        self.is_running = False

    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            print(f"{self.brand} {self.model} started.")
        else:
            print("Cannot start. Fuel tank is empty.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} stopped.")
        else:
            print("Car is already off.")

    def refuel(self, amount):
        if amount <= 0:
            print("Refuel amount must be positive.")
            return
        if self.fuel_level + amount > self.fuel_capacity:
            self.fuel_level = self.fuel_capacity
            print(f"{self.brand} {self.model} refueled to full capacity.")
        else:
            self.fuel_level += amount
            print(f"{self.brand} {self.model} refueled. Current fuel: {self.fuel_level}/{self.fuel_capacity}")

    def drive(self, distance):
        if not self.is_running:
            print("Start the car before driving.")
            return
        fuel_needed = distance * 0.1  # assume 0.1 units fuel per km
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"{self.brand} {self.model} drove {distance} km. Remaining fuel: {self.fuel_level:.1f}")
        else:
            print("Not enough fuel to drive that distance.")

    def display_car_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")
        print(f"Fuel: {self.fuel_level}/{self.fuel_capacity}")
        print(f"Running: {self.is_running}")


# Child class Toyota
class Toyota(Car):
    def start(self):
        super().start()  # call parent logic first
        if self.is_running:
            print(f"Toyota {self.model} roars to life with reliability!")

    def drive(self, distance):
        if not self.is_running:
            print("Toyota must be started before driving.")
            return
        fuel_needed = distance * 0.08  # Toyota is more fuel efficient
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"Toyota {self.model} smoothly covered {distance} km. Remaining fuel: {self.fuel_level:.1f}")
        else:
            print("Toyota does not have enough fuel for this trip.")


# Child class Audi
class Audi(Car):
    def start(self):
        super().start()  # reuse parent logic
        if self.is_running:
            print(f"Audi {self.model} starts with luxury and precision!")

    def drive(self, distance):
        if not self.is_running:
            print("Audi must be started before driving.")
            return
        fuel_needed = distance * 0.12  # Audi consumes more fuel
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"Audi {self.model} powered through {distance} km. Remaining fuel: {self.fuel_level:.1f}")
        else:
            print("Audi does not have enough fuel for this journey.")
