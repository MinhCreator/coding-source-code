import random
import names


def Random_pass():



    #variables to storage character, number and symbol
    character_lower_case = "qwertyuiopasdfghjklzxcvbnm"

    character_up_case = "QWERTYUIOPASDFGHJKLZXCVBNM" 

    numbers = "0123456789"


    symbol = "!@#$%^&*?/"

    #combine character, number and symbol

    Use_for = character_lower_case + character_up_case + numbers + symbol

    #length for password
    length_for_password = 16

    #random password
    password = "".join(random.sample(Use_for, length_for_password))

    #print to password

    # print("email password:", password)

    return f'password: {password}'


def generate_email_and_user_name():


    #var to storage generater name

    first_name = names.get_first_name(gender = any)

    last_name = names.get_last_name()

    print('first name:', first_name)

    print('last name:', last_name)

    character_lower_case = "qwertyuiopasdfghjklzxcvbnm"

    numbers = "0123456789"
    #combine character, number and name

    q = character_lower_case + numbers
    
    #length for password
    length_for_name = 4

    random_sub = "".join(random.sample(q, length_for_name))

    name = first_name + last_name + random_sub

    n = '@gmail.com'

    #combine

    combine = name + n

    # print('email:', combine)

    return f'email: {combine}'

def anonymous(key):

     key = str(key)

     if key == "Key.f12":
           raise SystemExit(0)


def check_function():

  

    print(generate_email_and_user_name())

    print(Random_pass())



print(check_function())

# run_function_email = str(input("generate email on or off:"))

# run_function_password = str(input("generate password on or off:"))

# check_function(active_or_inactive, run_function_email, run_function_password)

