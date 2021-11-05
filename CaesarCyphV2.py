crypt(text):
        result = ""
        for i in range(len(cypher_text)):
                char_position = ord(cypher_text[i])
                if(char_position >= 97) and (char_position <= 122):
                        char_position = char_position - 97
                        new_char_position = char_position - 3
                        new_char_position = new_char_position % 26
                        new_char_position = new_char_position + 97
                        result = result + chr(new_char_position)
                        print(result)
                elif (char_position >= 65) and (char_position <= 90):
                        char_position = char_position - 65
                        new_char_position = char_position - 3
                        new_char_position = char_position % 26
                        new_char_position = new_char_position + 65
                        result = result + chr(new_char_position)
                        print(result)
        return result

text = "GeneralMalaise"
text2 = "CheechANNNDChong"

print(f"Plain Text: {text}")
cypher_text = caesar_encrypt(text)
print(f"Encrypted: {cypher_text}")
print(f"Decrypted: {caesar_decrypt(cypher_text)}")

print(f"Plain Text2: {text2}")
cypher_text = caesar_encrypt(text2)
print(f"Encrypted: {cypher_text}")
print(f"Decrypted: {caesar_decrypt(cypher_text)}")
