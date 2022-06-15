#!/usr/bin/env python3

from cmath import pi
from tkinter import N
from turtle import position


class Engine:
    type = ''
    rpm = 0

    def __init__(self, type, rpm):
        self.type = type
        self.rpm = rpm

    def __str__(self):
        return f'Engile( type={self.type}, rpm={self.rpm} )'


class Car:
    brand = ''
    engine = None
    diameter_wheels = 0
    position = 0

    def __init__(self, brand, engine, diameter_wheels):
        self.brand = brand
        self.engine = engine
        self.diameter_wheels = diameter_wheels

    def move(self, time):
        if(self.engine):
            self.position = self.diameter_wheels*pi*self.engine.rpm*time
        else:
            self.position = 0

    def __str__(self):
        return f"Car( brand={self.brand}, engine={self.engine}, diameter_wheels={self.diameter_wheels}, position={self.position} )"


def find_the_fastest(list_of_cars, time):
    distances = []
    for aCar in list_of_cars:
        aCar.move(time)
        distances.append(aCar.position)

    max_value = max(distances)
    max_index = distances.index(max_value)
    return list_of_cars[max_index]


car1 = Car('Mercedes', Engine('diesel', 2000), 1.5)
car2 = Car('Mercedes', Engine('diesel', 3500), 1.0)

res = find_the_fastest([car1, car2], 10)
print('The fastest: ', res)
