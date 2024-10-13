"""Convert values in temps_input.txt from Fahrenheit to Celsius"""

# import random
#
# with open("temps_input.txt", "w") as out_file:
#     for i in range(15):
#         print(random.uniform(-200, 200), file=out_file)

from temperatures import calculate_celsius


def main():
    with open("temps_output.txt", "w") as out_file:
        with open("temps_input.txt", "r") as in_file:
            for line in in_file:
                fahrenheit = float(line)
                celsius = calculate_celsius(fahrenheit)
                print(celsius, file=out_file)


main()
