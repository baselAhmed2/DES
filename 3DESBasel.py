from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# ================================
# المفتاح الافتراضي لـ 3DES (لازم يكون 16 أو 24 بايت)
DEFAULT_KEY = b'1234567812345678'  # 16 بايت

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
user_key = input("Enter 16 or 24-character key (or press Enter to use default key): ")

if user_key == "":
    key = DEFAULT_KEY
    print("Using default key:", DEFAULT_KEY)
else:
    if len(user_key) not in [16, 24]:
        print("Key must be exactly 16 or 24 characters!")
        exit()
    key = user_key.encode()

# ================================
# اختيار العملية
choice = input("Type E for Encryption or D for Decryption: ").lower()

# ================================
# إنشاء كائن 3DES
des3 = DES3.new(key, DES3.MODE_ECB)

# تشفير
if choice == 'e':
    cipher_text = des3.encrypt(plaintext)
    print("\nEncrypted text (bytes):", cipher_text)
    print("Encrypted text (hex)  :", cipher_text.hex())

# فك التشفير
elif choice == 'd':
    decrypted = des3.decrypt(plaintext)
    print("\nDecrypted text:", decrypted.decode())

else:
    print("Invalid choice! Please enter E or D.")
