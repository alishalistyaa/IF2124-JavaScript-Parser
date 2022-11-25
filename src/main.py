# File: main.py
# Program yang memparser java script

import os
from utils.token import getTokens
from utils.Grammar.fileprocessing import *
from utils.parsingalgo import parsingCYK

# splash screen intro

print("Pastikan file sudah ada di folder src/test.")
filename = input("Masukkan nama file javascript yang akan di-parse: ")

filename = os.path.join(os.getcwd(),"test/" + filename)

while (not(os.path.isfile(filename) and filename.endswith(".js"))):
    print(f"\nFile tidak ditemukan atau tidak valid. Silakan masukkan nama file yang benar.\n")
    print("Pastikan file sudah ada di folder src/test.")
    filename = input("Masukkan nama file javascript yang akan di-parse: ")
    
tokens, errInfo = getTokens(filename)

if (errInfo[1] == -1):
    print("TOKENS")
    print(tokens)
    cfg = readGrammarFile(os.path.join(os.getcwd(),"utils/Grammar/grammar.txt"))
    cnf = convertGrammar(cfg)
    parsingCYK(tokens, cnf)
else:
    print(f"Syntax Error: Karakter ilegal terdeteksi pada {errInfo[0]}, baris ke-{errInfo[1]}, kolom ke-{errInfo[2]}.")
    
# splash screen outro