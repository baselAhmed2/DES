alpha_map = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f',
    6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
    12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
    18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x',
    24: 'y', 25: 'z'
}

char_to_num = {letter: idx for idx, letter in alpha_map.items()}

while True:
    message = input("Enter text: ").lower()
    shift_val = int(input("Enter key: "))

    cipher_text = ""
    plain_text = ""

    # --- Encryption phase ---
    for symbol in message:
        if symbol in char_to_num:
            num = char_to_num[symbol]
            new_num = (num + shift_val) % 26
            cipher_text += alpha_map[new_num]
        else:
            cipher_text += symbol

    # --- Decryption phase ---
    for symbol in cipher_text:
        if symbol in char_to_num:
            num = char_to_num[symbol]
            old_num = (num - shift_val) % 26
            plain_text += alpha_map[old_num]
        else:
            plain_text += symbol

    print("Encrypted:", cipher_text)
    print("Decrypted:", plain_text)
