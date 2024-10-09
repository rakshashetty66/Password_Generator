import random
print("Welcome to the Password Generator!")

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '?']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n_letters = int(input("How many letters Would you like in your Password? "))
n_symbols = int(input("How many symbols Would you like? "))
n_numbers = int(input("How many numbers Would you like? "))

password_list = []

for i in range(1, n_letters + 1):
    char = random.choice(letters)
    password_list += char

for i in range(1, n_symbols + 1):
    char = random.choice(symbols)
    password_list += char

for i in range(1, n_numbers + 1):
    char = random.choice(numbers)
    password_list += str(char)  # Convert number to string to add it to the list

random.shuffle(password_list)
print(password_list)

password = ""
for i in password_list:
    password += i  # Use i instead of char to append each character from the list

print(password)
