from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'ABCDEFGH'
plaintext = b'Hello Yousif DES!'

cipher = DES.new(key, DES.MODE_ECB)

padded_text = pad(plaintext, DES.block_size)
ciphertext = cipher.encrypt(padded_text)

decrypted_padded = cipher.decrypt(ciphertext)
decrypted_text = unpad(decrypted_padded, DES.block_size)

print("Plaintext:", plaintext.decode())
print("Ciphertext (hex):", ciphertext.hex())
print("Decrypted:", decrypted_text.decode())

