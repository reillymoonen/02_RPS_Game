# Functions go here
def choice_checker(question):

    valid = False
    while not valid:

        # Ask user for choice
        responce = input(question)

        if responce == "r" or responce == "rock":
            return responce


# Main routine goes here

# Ask user for choice and check it's valid
user_choice = choice_checker("Choose rock / paper/ "
                             "scissors (r/p/s): ")


# Print out choice for comparison purposes
