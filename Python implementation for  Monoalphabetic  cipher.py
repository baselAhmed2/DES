import string
import random
# -------------------
#? Generate Random Key
# --------------------
def generate_key():
    letters = list(string.ascii_uppercase)
    shuffled = letters.copy()
    random.shuffle(shuffled)
    key = dict(zip(letters, shuffled))
    return key

# --------------------
#? Encrypt
# --------------------
def encrypt(text, key):
    text = text.upper()
    encrypted = ""
    for char in text:
        if char in key:
            encrypted += key[char]
        else:
            encrypted += char
    return encrypted

# --------------------
#? Decrypt
# --------------------
def decrypt(cipher_text, key):
    reverse_key = {v: k for k, v in key.items()}
    decrypted = ""
    for char in cipher_text:
        if char in reverse_key:
            decrypted += reverse_key[char]
        else:
            decrypted += char
    return decrypted


# --------------------
#? Main Menu
# --------------------
print("Choose an option:")
print("1 - Encrypt")
print("2 - Decrypt")

choice = input("Enter choice: ")

# --------------------
#? ENCRYPT
# --------------------
if choice == "1":
    word = input("Enter word to encrypt: ").upper()

    print("\nChoose key option:")
    print("1 - Enter my own key")
    print("2 - Generate random key")

    key_choice = input("Enter choice: ")

    # --- User provides key ---
    if key_choice == "1":
        print("\nEnter substitution key (26 letters in order).")
        print("Example: QWERTYUIOPASDFGHJKLZXCVBNM")
        key_input = input("Key: ")

        alphabet = list(string.ascii_uppercase)
        key = dict(zip(alphabet, list(key_input)))

    # --- Random key generated ---
    elif key_choice == "2":
        key = generate_key()
        print("\nGenerated Random Key:")
        print("".join(key.values()))

    else:
        print("Invalid key option!")
        exit()

    cipher = encrypt(word, key)
    print("\nEncrypted:", cipher)


# --------------------
#? DECRYPT
# --------------------
elif choice == "2":
    cipher_text = input("Enter encrypted word: ").upper()

    print("Enter the same substitution key used for encryption.")
    key_input = input("Key: ").upper()

    alphabet = list(string.ascii_uppercase)
    key = dict(zip(alphabet, list(key_input)))

    decoded = decrypt(cipher_text, key)
    print("\nDecrypted:", decoded)

else:
    print("Invalid choice!")
# --------------------
# --------------------
print ("\n---  \n  Made By Basel Ahmed 512393207 ---\n")
