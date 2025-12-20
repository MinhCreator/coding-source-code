import random
def Random_pass(opts: int):
    #variables to storage character, number and symbol
    character_lower_case = "qwertyuiopasdfghjklzxcvbnm"
    character_up_case = "QWERTYUIOPASDFGHJKLZXCVBNM" 
    numbers = "0123456789"
    symbol = "!@#$%^&*?\/"
    #combine character, number and symbol
    Use_for = character_lower_case + character_up_case + numbers + symbol
    #length for password
    length_for_password = [16, 18, 20, 64, 128, 256]
    #random password
    password = "".join(random.sample(Use_for, length_for_password[opts]))
    #print to password
    # print("email password:", password)
    return password

path = "source-code\code_testing\password.txt"

with open(path, "w") as file:

    print(Random_pass(int(input("choose length for password: "))), file = file)


