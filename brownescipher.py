def decrypt_text_1798(text):
    decrypted_text = ""
    decrypt_dict = {'b':'a', 'r':'e', 'o':'i', 'w':'o', 'n':'u', 'e':'y'}
    for letter in text:
        if letter.lower() in decrypt_dict:
            decrypted_text += decrypt_dict[letter.lower()]
        else:
            decrypted_text += letter
    return decrypted_text

def encrypt_text_1798(text):
    encrypted_text = ""
    encrypt_dict = {'a':'b', 'e':'r', 'i':'o', 'o':'w', 'u':'n', 'y':'e'}
    for letter in text:
        if letter.lower() in encrypt_dict:
            encrypted_text += encrypt_dict[letter.lower()]
        else:
            encrypted_text += letter
    return encrypted_text

def decrypt_text_1802(text):
    decrypted_text = ""
    decrypt_dict = {'k':'a', 'c':'e', 'o':'i', 'l':'o', 'n':'u', 'u':'y'}
    for letter in text:
        if letter.lower() in decrypt_dict:
            decrypted_text += decrypt_dict[letter.lower()]
        else:
            decrypted_text += letter
    return decrypted_text

def encrypt_text_1802(text):
    encrypted_text = ""
    encrypt_dict = {'a':'k', 'e':'c', 'i':'o', 'o':'l', 'u':'n', 'y':'u'}
    for letter in text:
        if letter.lower() in encrypt_dict:
            encrypted_text += encrypt_dict[letter.lower()]
        else:
            encrypted_text += letter
    return encrypted_text

cipher = input("Please enter the type of cipher you want to use (1798 or 1802): ")

if cipher == "1798":
    operation = input("Do you want to encrypt or decrypt the text? (E/D): ").lower()
    text = input("Please enter the text you want to decrypt: ")
    if operation == "e":
        print("Encrypted text: ", encrypt_text_1798(text))
    elif operation == "d":
        print("Decrypted text: ", decrypt_text_1798(text))
    else:
        print("Invalid operation")
elif cipher == "1802":
    operation = input("Do you want to encrypt or decrypt the text? (E/D): ").lower()
    text = input("Please enter the text you want to decrypt: ")
    if operation == "e":
        print("Encrypted text: ", encrypt_text_1802(text))
    elif operation == "d":
        print("Decrypted text: ", decrypt_text_1802(text))
    else:
        print("Invalid operation")
else:
    print("Invalid cipher type")
