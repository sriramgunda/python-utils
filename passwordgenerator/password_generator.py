import string
import random

#properties
all_aplhabets = string.ascii_letters
dgts = string.digits
special_chars = string.punctuation

all_combo_keys = all_aplhabets + dgts + special_chars

def randomPassword(password_length = 10):
    '''
    Generate random password with default length of 10 characters.
    Password contains combination of alpha numeric and special characters.
    '''
    random_keys = [random.choice(all_combo_keys) for i in range(password_length)]
    return ''.join(random_keys)


if __name__ == '__main__':
    #default length of random password
    print(randomPassword())
    #8 characters length of password
    print(randomPassword(password_length = 8))
