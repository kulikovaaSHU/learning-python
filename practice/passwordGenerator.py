import random


def random_pick(min_num, max_num):
    new_random = random.randint(min_num-1, max_num)
    return new_random


def random_symbol():
    symbols = ["!","@","#","$","%","^","&","*","(",")","_","-","+","~","`","[","]","{","}",",",".","\\","/","|","?",":",
               ";"]
    new_symbol = symbols[random_pick(0,len(symbols)-1)]
    return new_symbol


def random_number():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    new_number = numbers[random_pick(0,len(numbers)-1)]
    return new_number


def random_letter():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    new_letter = letters[random_pick(0, len(letters)-1)]
    return new_letter

def uppercase_letter(letter):
    return letter.upper()


def generate_pass(length):
    i = 1
    new_pass = ""
    while i <= length:
        char_type = random_pick(1,3)
        if char_type == 0:
            symbol = str(random_symbol())
            new_pass += symbol
        elif char_type == 1:
            number = str(random_number())
            new_pass += number
        elif char_type == 2:
            letter = random_letter()
            new_pass += letter
        elif char_type == 3:
            letter_upper = random_letter()
            letter_upper = uppercase_letter(letter_upper)
            new_pass += letter_upper
        i += 1

    return new_pass


def main_function():
    pass_length = int(input("\nEnter desired length for password: "))
    print("Your new password: " + generate_pass(pass_length))
    again = input("\nTry again (Y or N): ")
    if again == "Y":
        main_function()
    else:
        print("\nGoodbye!")

print("Welcome to password generator.")
main_function()