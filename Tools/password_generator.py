import string
import random

def main():
    try:
        password_length = int(input("Enter the length of password: "))
        if password_length <= 0:
            raise ValueError
        print(generate_password(password_length))
    except ValueError:
        print("Invalid Length - Please enter a integer(greater than zero).")
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += (random.choice(characters))
    return password

if __name__=="__main__":
    main()