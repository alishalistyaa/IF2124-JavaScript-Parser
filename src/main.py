# File: main.py
# Program yang memparser java script

import os
from utils.token import createTextTokens

# splash screen intro
print(os.getcwd())
filename = 'hehe.js'
filename = input("Masukkan nama file .js yang akan di-parse: ")
filename = os.path.join(os.getcwd(),filename)
while (not(os.path.isfile(filename))):
    print(f"File {filename} tidak ditemukan. Silakan masukkan nama file yang benar.")
    filename = input("Masukkan nama file .js yang akan di-parse: ")
    
tokens, errInfo = createTextTokens(filename)
print(tokens)

if (errInfo[1] != 1):
    # lanjut parsing
    print(tokens)
else:
    print(f"Syntax Error: Karakter ilegal terdeteksi pada {errInfo[0]}, baris ke-{errInfo[1]}, kolom ke-{errInfo[2]}.")
    
# splash screen outro