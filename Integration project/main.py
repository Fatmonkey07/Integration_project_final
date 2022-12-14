__author__ = "Joe Ervin"
__email__ = "joeerv123@outlook.com"
__status__ = "Prototype"

if __name__ == "__main__":  # == is a boolean that checks if the values are
    # equal to each other.

    def main():
        # start menu
        print(
            "Welcome to my integration project.\nThis is a word game where you"
            " are given one letter of the word at a time and have ten guesses"
            " to correctly place all the letters.")

        start_options = "Start", "Exit"  # tuple with the options for the menu
        run_menu(
            start_options)  # calls run_menu function and passes start_options
        # as its only argument

        # Establishing the word
        open_file = open("$WORD_BANK$.txt", 'r')  # opens the word bank file
        word_bank = open_file.readlines()  # reads the lines of the file and
        open_file.close()  # closes the file

        from random import \
            choice  # imports the choice package from the random library

        word = choice(
            word_bank)  # choice function takes a random element from a list
        word = word.rstrip()  # gets rid of the end characters which is \n
        # because of how the word was read in
        word_length = len(word)
        guess_counter = 10  # starts the guess_counter at 10 so that the player
        # has 10 guesses
        round_over = False  # variable for whether the round should end

        letters = list(
            word)  # turns the word into a list that is split up by each letter
        unknown_letters = list(word)
        known_letters = ["_"] * word_length  # sets up the known letters
        # list so that each element is an underscore until that letter of the
        # word is known.
        positions_found = []  # list to keep track of which letter positions
        # have been found.

        # Establishing letter

        chosen_letter = choice(letters)  # gets a random letter from the word.

        while not round_over:  # while loop is a loop used when the number of
            # iterations are unknown. This loop ends when round_over == True.

            # find out if round should be over.
            if known_letters == letters:  # checks if all letters are known.
                round_over = True
                finish(word, guess_counter,
                       True)  # calls the finish function to end the game.
            elif guess_counter <= 0:  # checks if the player is out of guesses.
                round_over = True
                finish(word, guess_counter, False)

            # sets up the user interface.
            print()
            print("Try to guess the word in 10 or less guesses.")
            print("type M or MENU to access the menu.")
            print(
                f"Guesses left:{guess_counter}")  # f'' formats a string so
            # that the value within the {} is inserted
            # into the string.

            display_word(word,
                         known_letters)  # calls the display word function to
            # display the positions of the word.

            print(
                "Guess where the letter", chosen_letter.upper(),
                "goes in the word.")  # .upper() returns the uppercase
            # of a string.
            guess = input("enter a number between 1 and " + str(
                word_length) + ":")  # player inputs their guess.
            while guess == "":  # loop so that if the player enters nothing
                # they get to input again.
                guess = input("Please enter an answer:")

            # interpret guess

            guess_type = input_type(guess, word,
                                    positions_found)  # calls input_type
            # function to figure out what kind of input the player gave.

            match guess_type:  # match statement is similar to if elif
                # structure. It compares the selected variable to the values of
                # each case and runs the code if they match.
                case "valid_integer":  # if guess_type == "valid_integer",
                    # this code is run.
                    guess = int(
                        guess) - 1  # int returns the integer of a string.
                    if letters[guess] == chosen_letter:  # [] accesses a
                        # specific index of a list.
                        print("Correct!")
                        known_letters[guess] = chosen_letter
                        unknown_letters.remove(
                            chosen_letter)  # .remove removes all instances
                        # of an element from a list
                        positions_found.append(
                            guess)  # .append adds the element to the end of a
                        # list.
                        if len(unknown_letters) > 0:  # > is a boolean that
                            # checks if the first value is greater than
                            # the second value.
                            chosen_letter = choice(unknown_letters)
                    else:
                        print("Incorrect :(")

                    guess_counter -= 1  # -= subtracts from the value. ex. -= 1
                    # subtracts 1 from the variable's value.

                case "invalid_integer":
                    print(
                        "That is not a valid number. Please enter a number "
                        "between 1 and", word_length)
                case "found_integer":
                    print(
                        f"letter position {guess} has already been found. "
                        f"Please enter a different number.")
                case "menu":
                    options = "Resume", "Guess word", "Restart", "Exit"
                    guess_counter = run_menu(options, word, known_letters,
                                             guess_counter)
                    continue
                case "invalid_answer":
                    print("That is not a valid answer.")

            print("...")


    def display_word(word_parameter,
                     known_parameter):  # defines display_word function to
        # display information about the word.

        # Expects: word, known letters
        # Modifies: Nothing
        # Returns: Nothing

        for number_counter in range(
                len(word_parameter)):  # for loop is a loop used when the
            # number of iterations is known. in is used to iterate through
            # the sequence.
            print(number_counter + 1,
                  end=" ")  # end changes what the end character is.
        print()
        for letter_counter in range(0, len(word_parameter)):
            print(known_parameter[letter_counter],
                  end=(" " * len(str(letter_counter + 1))))
        print("\n")


    # figuring out the type of input the user gave.
    def input_type(guess_parameter, word_parameter,
                   positions_found_parameter=None):  # defines the input_type
        # function to figure out what kind of input the user gave.

        # Expects: player's guess, word, positions_found
        # Modifies: Nothing
        # Returns: guess_type string

        try:
            if 0 <= int(guess_parameter) <= len(word_parameter):
                guess_parameter = int(guess_parameter) - 1
                if int(guess_parameter) in positions_found_parameter:
                    return "found_integer"  # return keyword returns whatever
                    # is after it from the function.
                else:
                    return "valid_integer"
            else:
                return "invalid_integer"
        except ValueError:
            if guess_parameter.lower() == "menu" or \
                    guess_parameter.lower() == "m":
                # .lower() returns an all lowercase version of the string.
                return "menu"
            else:
                return "invalid_answer"


    def run_menu(menu_options, word_parameter=None, known_parameter=None,
                 guesses=None):  # defines the run_menu function to create and
        # run a menu out of the arguments it is given.

        # Expects: options for menu, word, known letters, guesses
        # Modifies: guesses and found
        # Returns: guesses

        while True:
            print("MENU\n")  # header

            for count, option in enumerate(menu_options):
                print(f"{count + 1}. {option}\n")
            while True:
                inp = input(
                    f"Enter your choice or the number corresponding to that "
                    f"choice:")
                try:  # tries the code and stops if it reaches an error without
                    # crashing.
                    inp = int(inp) - 1
                    if inp in range(len(menu_options)):
                        selected = menu_options[inp]
                        break  # breaks out of the loop.
                    else:
                        print("That is not a valid number.\n")

                except ValueError:  # if the code in the try statement produces
                    # a ValueError, this code is run.
                    if inp.lower() in map(str.lower,
                                          menu_options):  # this map function
                        # returns the lowercase version of each menu option so
                        # that it isn't cap sensitive.
                        selected = inp[0].upper() + inp[
                                                    1:]  # changes the string
                        # so that the first letter is uppercase.
                        break
                    print("That is not a valid number.\n")

            match selected:
                case "Start":
                    print("Starting Game...")
                    return
                case "Resume":
                    print("Resuming game...")
                    return guesses
                case "Guess word":
                    display_word(word_parameter, known_parameter)
                    guess = input(
                        "type your guess or type 1 or BACK to return to the "
                        "menu:")
                    while not guess.isalpha() and guess != "1":  # not returns
                        # the opposite so if it would've been false then it
                        # returns true. and means both conditions must return
                        # true for the condition to be true.
                        guess = input("please type a valid word:")

                    if guess.lower() == word_parameter:
                        print("Correct!")
                        finish(word_parameter, guesses - 1, True)
                        return
                    elif guess.lower() == "back" or guess == "1":
                        print("Returning to menu...")
                        pass
                    else:
                        print("That is incorrect :(")
                        guesses -= 1
                case "Restart":
                    print("Restarting game...")
                    main()
                    return
                case "Exit":
                    exit()


    def finish(word_parameter, guesses,
               found):  # defines finish function that finishes the game.
        # Expects: The word, how many guesses are left, and if the word was
        # found
        # Modifies: Nothing
        # Returns: Nothing

        if found:  # runs indented code if the player found the word
            print(
                f"congratulations! You've found the full word {word_parameter}"
                f"in only {10 - guesses} guesses.\n")
        else:  # runs indented code if the player did not find the word
            print(
                f"Unfortunately, you were unable to find the word in 10 "
                f"guesses.")
        options = "Restart", "Exit"
        run_menu(options, word_parameter)  # calls the run_menu function


    def sprint_1_reqs(value):
        value_sqr = value ** 2  # ** raises the first value to the power of
        # the second value.
        value_doubled = value * 2  # * multiplies the first value by the
        # second value.
        value_halved = value / 2  # / divides the first value by the second
        # value.
        value_remainder = value % 2  # takes the first value divided by the
        # second value and returns the remainder of that division.
        value_half_floored = value // 2  # divides the first value by the
        # second value and returns the integer of the division
        print(value_sqr, value_doubled, value_halved, value_remainder,
              value_half_floored, sep="|",
              end="|")  # sep changes
        # what separates the arguments in the print statement. end changes
        # the end character.

    main()
