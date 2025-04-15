"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_BAKE_TIME = 2

print("Welcome to Our Guido's Lasagna Preparation!!")
baking = input("Do you want to start? ")

if baking != "yes":
    quit()
print("Let's bake!")


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    bakeTimeR = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bakeTimeR 


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(number_of_layers):
    preparationT = PREPARATION_BAKE_TIME * number_of_layers
    return preparationT

#TODO: define the 'elapsed_time_in_minutes()' function below.

def elasped_time_in_minutes(number_of_layers, elapsed_bake_time):
    total_elapsed_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_elapsed_time
    


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)


number_of_layers = int(input("How many layers do you want to prepare? "))
print(f"You have {number_of_layers} layers.")
preparationT = preparation_time_in_minutes(number_of_layers)
print(f"Your preparation time would be {preparationT} minutes.")

elapsed_bake_time =int(input("How long has Lasagna been in the oven so far? "))
print(f"Your elapsed bake time is {elapsed_bake_time} minutes.")
bakeTimeR = bake_time_remaining(elapsed_bake_time)
print(f"Your expected bake time is {EXPECTED_BAKE_TIME} minutes.")
print(f"Your remaining bake time is {bakeTimeR} minutes.")

total_elasped_time = elasped_time_in_minutes(number_of_layers, elapsed_bake_time)
print(f"Your total elapsed time is {total_elasped_time} minutes. Enjoy!")

