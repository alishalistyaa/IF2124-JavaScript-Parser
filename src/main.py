# File: main.py
# Program yang memparser java script

import os
from utils.token import getTokens
from utils.Grammar.fileprocessing import *
from utils.parsingalgo import *

# splash screen intro

print("Pastikan file sudah ada di folder src/TestCase.")
filename = input("Masukkan nama file javascript yang akan di-parse: ")

filename = os.path.join(os.getcwd() + "/TestCase/" + filename)

while (not(os.path.isfile(filename) and filename.endswith(".js"))):
    print(f"\nFile tidak ditemukan atau tidak valid. Silakan masukkan nama file yang benar.\n")
    print("Pastikan file sudah ada di folder src/TestCase.")
    filename = input("Masukkan nama file javascript yang akan di-parse: ")
    filename = os.path.join(os.getcwd() + "/TestCase/" + filename)
    
tokens, errInfo = getTokens(filename)

if (errInfo[1] == -1):
    cfg = readGrammarFile(os.path.join(os.getcwd(),"utils/Grammar/revG.txt"))
    cnf = convertGrammar(cfg)
    cnfdict = makeDictionary(cnf)
    parsingCYK(tokens, cnfdict)
else:
    print(f"Syntax Error: Karakter ilegal terdeteksi pada {errInfo[0]}, baris ke-{errInfo[1]}, kolom ke-{errInfo[2]}.")
    
# splash screen outro