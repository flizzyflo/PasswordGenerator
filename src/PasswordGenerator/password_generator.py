from random import randint
from Settings.settings import MIN_LENGTH, MAX_LENGTH, CHARACTER_LIST

def generate_password(password_length: int) -> str:
    
    """Generates a password consisting out of several elements 
    from lower- and uppercase, digits and punctuation elements.
    
    #### Parameters
    1. password_length: int
        -- specifies the lenght of the password
   
    #### Returns
    1. password: str
        -- Password as a string with length of input argument as a string.

    """

    # not required since the gui itself checks for the MIN and MAX lenght. 
    # Commented, usable if password generation is used without gui
    
    # if password_length < MIN_LENGTH:
    #     return "password is to short to be considered secure"
    
    # if password_length > MAX_LENGTH:
    #     return "Password length is to big to create password with every letter occuring once"

    gen_count: int = 0
    password: str  = ""
    variety_counter: int = 0

    while gen_count < password_length:

        # if statement is false as long as not at least one letter from every letter type is used
        # ensures that a character from every single type of characters is included into password
        if variety_counter < len(CHARACTER_LIST) - 1:
            letter_type = variety_counter
            variety_counter += 1

        else:
            # random selection of remaining characters to complete the password 
            letter_type = randint(0, len(CHARACTER_LIST) - 1)

        letter_index = randint(0, len(CHARACTER_LIST[letter_type]) - 1) #selection of the letter out of the string
        letter_to_add = CHARACTER_LIST[letter_type][letter_index] #store letter selected

        if letter_to_add not in password:
            # ensures that every character is used solely within the password generated
            password += CHARACTER_LIST[letter_type][letter_index]
            gen_count += 1
        
    return password
