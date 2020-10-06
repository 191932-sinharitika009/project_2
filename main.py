import random
class Psswrd:
    def pswrd_creator(self):
        lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

        upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

        numeric_case = ['0', '2', '3', '4', '5', '1', '6', '7', '8']

        special_case = ['!', '@', '_', '.', ',', '`']

        password = random.choice(lower_case) + random.choice(upper_case) + random.choice(numeric_case) + random.choice(
            special_case)
        new=2*password
        return new


pswrd=Psswrd()
print(pswrd.pswrd_creator())

