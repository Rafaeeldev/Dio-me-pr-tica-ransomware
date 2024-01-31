import os
import pyaes

file_name = "teste.txt.ransomwareTroll"
filee = open(file_name, "rb")
file_data = filee.read()
filee.close()

key = b"testeransomware6"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = "teste.txt"
new_file = open(f"{new_file}", "wb")
new_file.write(decrypt_data)
new_file.close()