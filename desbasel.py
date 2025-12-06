from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

DEFAULT_KEY = b'12345678'

# ================================
# اختيار العملية
while True:
    choice = input("Type E for Encryption or D for Decryption: ").lower()

    # ================================
    # إدخال النص
    text = input("Enter text: ")
    plaintext = text.encode()

    # ================================
    # إدخال المفتاح
    user_key = input("Enter 8-character key (or press Enter for default key): ")

    if user_key == "":
        key = DEFAULT_KEY
        print("Using default key: 12345678")
    else:
        if len(user_key) != 8:
            print("Key must be exactly 8 characters!")
            exit()
        key = user_key.encode()

    # ================================
    # إنشاء DES
    des = DES.new(key, DES.MODE_ECB)

    # ================================
    # التشفير
    if choice == 'e':
        padded = pad(plaintext, DES.block_size)
        ciphertext = des.encrypt(padded)
        print("\nEncrypted (hex):", ciphertext.hex())

    # ================================
    # فك التشفير
    elif choice == 'd':
        try:
            ciphertext = bytes.fromhex(text)
            decrypted = des.decrypt(ciphertext)
            unpadded = unpad(decrypted, DES.block_size)
            print("\nDecrypted text:", unpadded.decode())
        except:
            print("Invalid ciphertext! Enter a valid hex string.")

    else:
        print("Invalid choice!")