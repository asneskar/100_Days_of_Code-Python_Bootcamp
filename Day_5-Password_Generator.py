import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n")) 
number_digits = int(input("How many numbers would you like?\n"))
number_symbols = int(input("How many symbols would you like?\n"))

number_characters = number_letters + number_digits + number_symbols
password_characters = []
password = ""

for random_letter in range(1, number_letters + 1):
  random_letter = random.randint(0, 51)
  random_letter = letters[random_letter]
  password_characters.append(random_letter)

for random_digit in range(1, number_digits + 1):
  random_digit = random.randint(0, 9)
  random_digit = digits[random_digit]
  password_characters.append(random_digit)

for random_symbol in range(1, number_symbols + 1):
  random_symbol = random.randint(0, 8)
  random_symbol = symbols[random_symbol]
  password_characters.append(random_symbol)

for random_character in range(1, number_characters + 1):
  random_character = random.randint(0, number_characters - 1)
  random_character = password_characters[random_character]
  number_characters -= 1
  password += random_character
  password_characters.remove(random_character)

print(password)
