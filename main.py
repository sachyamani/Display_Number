"""
Module to convert number to word
"""
import inflect


def get_words_for_number(num):
    """
    Function to convert given number into a word form.
    :param num: Integer - Number to convert into a word
    :return: String - Word form of the given number.
    """
    p = inflect.engine()
    return p.number_to_words(num)


def main(user_input):
    """
    A wrapper function to convert the user_input into integer and call get_words_for_number method
    :param user_input: String - A number in the form of string.
    :return: None / String - returns the word form if the string is valid else None.
    """
    try:
        user_input = int(user_input)
        return get_words_for_number(user_input)
    except ValueError:
        return None


if __name__ == '__main__':
    # Capturing User Input
    input_num = input('Enter a number: ')
    word = main(input_num)
    print(word or f"The given input ({input_num}) is not a valid integer")
