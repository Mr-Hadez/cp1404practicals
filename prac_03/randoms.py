"""
CP1404 - Practical
explore functions for random numbers
"""

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?

# I saw the number 11 which was randomly generated using the randint function. The smallest number I could have seen is 5 and the largest is 20.

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?

# I saw 7 which was randomly generated using the randrange function. All the numbers that could be generated were odd in range of 3 and 10, so the smallest number that...
# could be generated is 3 and the largest is 9. It is impossible to see a 4.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?

# I saw a long float value each time for line 3, randomly generated between 2.5 and 5.5, with 5.5 being inclusive depending on rounding. So the smallest number...
# is 2.5 and the largest is 5.5.

import random
random_number = random.randint(1,100)
print(random_number)
