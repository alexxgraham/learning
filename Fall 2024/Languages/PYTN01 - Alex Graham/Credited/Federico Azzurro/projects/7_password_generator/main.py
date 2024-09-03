# ----------------------------------------------------------------------
# |  main.py
# |
# |  by Federico Azzurro
# ----------------------------------------------------------------------
import secrets
import string


class Password:
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        self.base_characters: str = string.ascii_lowercase + string.digits

        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return ''.join(password)

def main() -> None:
    password: Password = Password(length=20, uppercase=True, symbols=True)
    for i in range(10):
        generated: str = password.generate()
        print(f'{generated} ({len(generated)} chars)')

if __name__ == '__main__':
    main()

"""
1. Create a method in the Password class which checks the passwords strength. 
- check that the password is more than 16 characters long
- check that the password both contains uppercase characters and symbols

"""
