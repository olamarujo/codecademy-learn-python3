# define a function to encrypt a message that needs the message to send and a keyword to be the key to encrypt
def vigenere_encode_func(message, keyword):

    # define every letter of the alphabet in a list
    alphabet = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # define the variable where the message will be stored
    my_msg_crip = ''
    # this number retpresents the letter used in the keywork to encrypt the letter of the message
    keyword_count = 0

    # a loop to run every letter of the message
    for letter in message:

        # if the caracter is a letter
        if letter.isalpha() == True:

            # Determine if uppercase or lowercase
            is_upper = letter.isupper()
            # Normalize to lowercase for indexing
            letter = letter.lower()

            # gets the index of the letter in message
            letter_index = alphabet.index(letter)
            # gets the index of the letter in keyword
            keyword_index = alphabet.index(keyword[keyword_count % len(keyword)].lower())

            # ENCRYPTION: add indices, wrap around using modulo
            new_index = (letter_index + keyword_index) % len(alphabet)
            new_letter = alphabet[new_index]

            # Restore original case
            if is_upper:
                new_letter = new_letter.upper()
            
            # adds new encrypted letter to the message
            my_msg_crip += new_letter

            # add 1 to keyword count to return the next letter next time
            keyword_count += 1

        # if the caracter is not a letter
        else:
            my_msg_crip += letter

    return my_msg_crip


my_msg_decrip = "Hello. I am Rodrigo and i wish you a very nice day!"
keyword = 'olamarujo'
print(vigenere_encode_func(my_msg_decrip, keyword))