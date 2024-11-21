"""Unreliable car test"""
from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("Prius 1",100, 65)
for i in range(1,11):
    my_car.drive(10)
print(my_car)
