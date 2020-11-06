# Import the needed packages
from textblob import TextBlob #use to determine the language of the string
import string


def countwords(inputs):
    # Counts the number of words and characters in the string
    # https://www.codevscolor.com/python-count-words-characters-string
    char_count = 0
    split_string = inputs.split()
    word_count = len(split_string)
    for word in split_string:
        if not word.isalpha() | word.isdigit():
            char_count += 1
    print("Total Words : {}".format(word_count))
    print("Total Special Characters : {}".format(char_count))


def findlanguage(inputs):
    # Uses Textblob to find the language of the inputted text
    words = TextBlob(inputs)
    print("Detected Language : ", words.detect_language())


def main():
    ourstring = 'hello my name is zenya, & I am a QF!'
    countwords(ourstring)
    findlanguage(ourstring)


if __name__ == "__main__":
    main()
