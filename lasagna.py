"""Preparing Guido's gorgeous lasagna.

This program calculates the total time needed to prepare lasagna.
It takes into account the preparation time and the baking time.
"""

EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2     # per layer, in minutes

def bake_time_remaining(elapsed_bake_time):
    """Return the remaining bake time."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Return total preparation time based on number of layers."""
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return total elapsed time: preparation + baking so far."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

def main():
    print("👋 Welcome to Our Guido's Lasagna Preparation!!")
    start = input("Do you want to start? (yes/no) ").strip().lower()

    if start != "yes":
        print("Alright, come back when you're hungry! 🍽️")
        return

    print("Let's bake! 🍝🔥")

    try:
        number_of_layers = int(input("How many layers do you want to prepare? "))
        print(f"You have {number_of_layers} layers.")
        
        preparation_time = preparation_time_in_minutes(number_of_layers)
        print(f"Your preparation time would be {preparation_time} minutes.")

        elapsed_bake_time = int(input("How long has the lasagna been in the oven so far? "))
        print(f"Your elapsed bake time is {elapsed_bake_time} minutes.")

        remaining_bake_time = bake_time_remaining(elapsed_bake_time)
        print(f"Expected total bake time is {EXPECTED_BAKE_TIME} minutes.")
        print(f"Your remaining bake time is {remaining_bake_time} minutes.")

        total_time = elapsed_time_in_minutes(number_of_layers, elapsed_bake_time)
        print(f"Your total elapsed time is {total_time} minutes. Enjoy your lasagna! 😋")

    except ValueError:
        print("⚠️ Please enter valid numbers only. Restart the program and try again.")
        return

if __name__ == "__main__":
    main()

