"""Silver service taxi test"""

from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer",200, 2)
print(my_taxi)
my_taxi.drive(18)
print(my_taxi)
print(my_taxi.get_fare())
