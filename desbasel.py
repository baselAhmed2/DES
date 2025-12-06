from Crypto.Cipher import DES

DEFAULT_KEY = b'12345678'   # الكي الافتراضي

# ================================
# ناخد النص من المستخدم
text = input("Enter 8-character text: ")

# لو النص أقل أو أكثر من 8 نوقف البرنامج
if len(text) != 8:
    print("Text must be exactly 8 characters!")
    exit()

plaintext = text.encode()


# ================================
# ناخد المفتاح من المستخدم
user_key = input("Enter 8-character key (or press Enter to use default key): ")

if user_key == "":
    key = DEFAULT_KEY
    print("Using default key: 12345678")
else:
    if len(user_key) != 8:
        print("Key must be exactly 8 characters!")
        exit()
    key = user_key.encode()


# ================================
# اختيار العملية
choice = input("Type E for Encryption or D for Decryption: ").lower()


# ================================
# إنشاء كائن DES
des = DES.new(key, DES.MODE_ECB)

# تشفير
if choice == 'e':
    result = des.encrypt(plaintext)
    print("\nEncrypted text (bytes):", result)
    print("Encrypted text (hex)  :", result.hex())

# فك التشفير
elif choice == 'd':
    result = des.decrypt(plaintext)
    print("\nDecrypted text:", result.decode())

else:
    print("Invalid choice! Please enter E or D.")


# ================================


from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# لازم طول المفتاح يكون 8 بايت بالظبط
key = b'12345678'    

# لازم طول النص يكون من مضاعفات 8
plaintext = b'HelloDES'

# إنشاء كائن التشفير
des = DES.new(key, DES.MODE_ECB)

# تشفير
cipher_text = des.encrypt(plaintext)
print("Encrypted:", cipher_text)

# فك التشفير
des2 = DES.new(key, DES.MODE_ECB)
decrypted = des2.decrypt(cipher_text)
print("Decrypted:", decrypted)
