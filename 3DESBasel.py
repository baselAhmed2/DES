from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

DEFAULT_KEY = b'1234567890123456'   # 16 bytes (default)

# ================================
while True:
    choice = input("\nType E for Encryption or D for Decryption: ").lower()

    # ================================
    # إدخال النص
    text = input("Enter text: ")
    plaintext = text.encode()

    # ================================
    # إدخال المفتاح
    user_key = input("Enter 16 or 24-character key (or press Enter for default key): ")

    if user_key == "":
        key = DEFAULT_KEY
        print("Using default key:", DEFAULT_KEY.decode())
    else:
        if len(user_key) not in [16, 24]:
            print("Key must be exactly 16 OR 24 characters!")
            continue
        key = user_key.encode()

    # ================================
    # إنشاء كائن 3DES
    des3 = DES3.new(key, DES3.MODE_ECB)

    # ================================
    # التشفير
    if choice == 'e':
        padding = pad(plaintext, DES3.block_size)
        ciphertext = des3.encrypt(padding)
        print("\nEncrypted (hex):", ciphertext.hex())

    # ================================
    # فك التشفير
    elif choice == 'd':
        try:
            ciphertext = bytes.fromhex(text)
            decrypted = des3.decrypt(ciphertext)
            unpadded = unpad(decrypted, DES3.block_size)
            print("\nDecrypted text:", unpadded.decode())
        except:
            print("Invalid ciphertext! Enter a valid hex string.")

    else:
        print("Invalid choice! Enter E or D.")
