"""This is a simple Caesar cypher program that will encode or decode the contents
of a text file.  The user must have a message text and a key to use these functions.
"""


#      CLOSE TO DONE, NEEDS SOME CLEAN UP OF MAIN() FLOW AND FORMATTING?  DOC STRINGS TOO  #

class Caesar:
    def caesar_encrypt(self, message: str, key: int):
        """Takes in a message string and a key, returns an encrypted string"""
        result = ''
        for letters in message:
            first_upper = 65
            first_lower = 97
            num_chars = 26

            # Encryption algorithm has some variable names changed but same logic.
            if ord(letters) == 32:
                result = result + chr(32)
            elif letters.islower():
                letters = str(letters)
                result += (chr((ord(letters) - first_lower + num_chars + key) % num_chars + first_lower))
            elif letters.isupper():
                letters = str(letters)
                result += (chr((ord(letters) - first_upper + num_chars + key) % num_chars + first_upper))
        return result

    def caesar_decrypt(self, message: str, key: int):
        """Takes in an encrypted string and a key, returns the original string"""
        first_upper = 65
        first_lower = 97
        num_chars = 26
        result = ''
        for letters in message:
            # Decryption algorithm has some variable names changed but same logic.
            if ord(letters) == 32:
                result = result + chr(32)
            elif letters.islower():
                letters = str(letters)
                result += (chr((ord(letters) - first_lower + num_chars - key) % num_chars + first_lower))
            elif letters.isupper():
                letters = str(letters)
                result += (chr((ord(letters) - first_upper + num_chars - key) % num_chars + first_upper))
        return result


def process_file(input_filename: str, output_filename: str, encode_decode: str, cypher_key: int):
    """This function will handle file operations, reading/writing to/from file and returning
    whether the process has run successfully or failed.
    """
    caesar_object = Caesar()
    if encode_decode == 'encode':
        try:
            with open(input_filename, 'r') as input_file:
                with open(output_filename, 'w') as output_file:
                    output_file.write(caesar_object.caesar_encrypt(input_file.read(), cypher_key))

        except FileNotFoundError:
            print("Oops, your source file is missing!")
            return False
    elif encode_decode == 'decode':
        try:
            with open(input_filename, 'r') as input_file:
                with open(output_filename, 'w') as output_file:
                    output_file.write(caesar_object.caesar_decrypt(input_file.read(), cypher_key))

        except FileNotFoundError:
            print("Oops, your source file is missing!")
            return False


def main():
    print("Hello, welcome to the Caesar Cypher encoder/decoder program.".center(100))
    print("This program will encode or decode the contents of a text (.txt) file.\n".center(100))
    while True:
        encode_decode = input(f"To encode respond with 'encode', to decode respond with 'decode'.\n"
                              f"Would you like to encode or decode a file's contents? ")
        if encode_decode == 'encode':
            print("Don't forget to include the extension *.txt in your answer.")
            input_filename = input("Enter the name of the file you want to encode: ")
            output_filename = input("Enter the name of the file you want to output your results to: ")
            cypher_key = int(input("Finally, what is your cypher key (integer)?  "))
            try:
                process_file(input_filename, output_filename, encode_decode, cypher_key)
                return True
            except FileNotFoundError as e:
                print("Something went wrong!")
                return False

        elif encode_decode == 'decode':
            print("Don't forget to include the extension *.txt in your answer.")
            input_filename = input("Enter the name of the file you want to decode: ")
            output_filename = input("Enter the name of the file you want to output your results to: ")
            cypher_key = int(input("Finally, what is your cypher key (integer)?  "))
            try:
                process_file(input_filename, output_filename, encode_decode, cypher_key)
                return True
            except FileNotFoundError as e:
                print("Something went wrong!")
                return False
        else:
            continue


if __name__ == "__main__":
    main()

""" --- Sample Run #1 --- 
   ----- encode ------
                    Hello, welcome to the Caesar Cypher encoder/decoder program.                    
              This program will encode or decode the contents of a text (.txt) file.
               
To encode respond with 'encode', to decode respond with 'decode'.
Would you like to encode or decode a file's contents? encode
Don't forget to include the extension *.txt in your answer.
Enter the name of the file you want to encode: message.txt
Enter the name of the file you want to output your results to: cyphertext.txt
Finally, what is your cypher key (integer)?  4
message.txt cyphertext.txt encode 4

Process finished with exit code 0


   ----- decode ------

                    Hello, welcome to the Caesar Cypher encoder/decoder program.                    
              This program will encode or decode the contents of a text (.txt) file.
               
To encode respond with 'encode', to decode respond with 'decode'.
Would you like to encode or decode a file's contents? decode
Don't forget to include the extension *.txt in your answer.
Enter the name of the file you want to decode: cyphertext.txt
Enter the name of the file you want to output your results to: decodedmessage.txt
Finally, what is your cypher key (integer)?  4

"""
