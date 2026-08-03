import random
import string

length = int(input("Enter password length (minimum 4): "))

if length < 4:
    print("Password length should be at least 4.")
else:
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    print("\nGenerated Password:", "".join(password))