import os
import pyaes

name = 'test.txt'
file = open(name,'rb')
file_data = file.read()
file.close()

os.remove(file)


key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
describe_data = aes.decrypt(file_data)


new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(describe_data)
new_file.close()