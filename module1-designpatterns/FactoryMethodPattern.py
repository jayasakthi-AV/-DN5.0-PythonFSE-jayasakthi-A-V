class Car:

    def drive(self):
        print("Driving Car")


class Bike:

    def drive(self):
        print("Driving Bike")


class VehicleFactory:

    @staticmethod
    def create(vehicle):

        if vehicle == "car":
            return Car()

        elif vehicle == "bike":
            return Bike()


vehicle = VehicleFactory.create("bike")

vehicle.drive()