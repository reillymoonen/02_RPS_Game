# Functions go here
def choice_checker(question: object) -> object:


    error = "Please choose from rock / paper/ " \
            "scissors (or xxx to quit)"

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        responce = input(question).lower()

        if responce == "r" or responce == "rock":
            return responce
        elif responce == "p" or responce == "paper":
            return responce
        elif responce == "s" or responce == "scissors":
            return responce

        # check for exit code
        elif responce == "xxx":
            return responce
        else:
            print(error)


# Main routine goes here


# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper/ "
                                 "scissors (r/p/s): ")

    # Print out choice for comparison purposes
    print("You choose {}".format(user_choice))
