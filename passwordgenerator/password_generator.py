import string
import random

#properties
all_aplhabets = string.ascii_letters
dgts = string.digits
special_chars = string.punctuation

all_combo_keys = all_aplhabets + dgts + special_chars
alpha_numeric_combo_keys = all_aplhabets + dgts

def randomPassword(password_length = 10):
    '''
    Generate random password with default length of 10 characters.
    Password contains combination of alpha numeric and special characters.
    '''
    random_keys = [random.choice(all_combo_keys) for i in range(password_length)]
    return ''.join(random_keys)


def randomPassword_alpha_numeric(password_length = 10):
    '''
    Password contains combination of alpha numeric with default length as 10 chars.
    '''
    random_keys = [random.choice(alpha_numeric_combo_keys) for i in range(password_length)]
    return ''.join(random_keys)


if __name__ == '__main__':
    #default length of random password
    print(randomPassword())
    #8 characters length of password
    print(randomPassword(password_length = 8))
    #generate alpha numeric hashkey
    print(randomPassword_alpha_numeric(password_length = 40))
