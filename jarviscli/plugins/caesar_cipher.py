from colorama import Fore
from plugin import plugin

@plugin("caesar cipher")
def caesar_cipher_converter(jarvis, s):
    option = get_option(jarvis)
    if option == 1:
        plain_to_cipher(jarvis)
    elif option == 2:
        cipher_to_plain(jarvis)
    # No need for else; get_option handles invalid choices.

def get_option(jarvis):
    jarvis.say("~> What can I do for you?", Fore.RED)
    print("1: Convert plain text to cipher")
    print("2: Convert cipher to plain text")
    print("3: Exit")
    print()

    while True:
        try:
            option = int(jarvis.input("Enter your choice: ", Fore.GREEN))
            if option == 3:
                return
            elif option in [1, 2]:
                return option
            else:
                jarvis.say("Invalid input! Enter a number from the choices provided.", Fore.YELLOW)
        except ValueError:
            jarvis.say("Invalid input! Enter a number from the choices provided.", Fore.YELLOW)
        print()

def caesar_cipher(text, shift):
    converted = ""
    for i in text:
        if i.isalpha():
            start = ord('A') if i.isupper() else ord('a')
            converted += chr((ord(i) - start + shift) % 26 + start)
        else:
            converted += i
    return converted

def plain_to_cipher(jarvis):
    user_input = get_user_input(jarvis)
    converted = caesar_cipher(user_input, 3)
    jarvis.say(converted, Fore.YELLOW)

def cipher_to_plain(jarvis):
    user_input = get_user_input(jarvis)
    converted = caesar_cipher(user_input, -3)
    jarvis.say(converted, Fore.YELLOW)

def get_user_input(jarvis):
    while True:
        try:
            user_input = jarvis.input("Enter string to convert: ")
            if len(user_input) > 0:
                return user_input
            else:
                jarvis.say("String length should be minimum 1.", Fore.YELLOW)
        except ValueError:
            jarvis.say("Sorry, I didn't understand that.", Fore.RED)
