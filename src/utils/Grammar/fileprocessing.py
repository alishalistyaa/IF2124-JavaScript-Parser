
terminal = [
    'break', 
    'const', 
    'case', 
    'catch', 
    'continue', 
    'default', 
    'delete', 
    'else', 
    'false', 
    'finally', 
    'for', 
    'function', 
    'if', 
    'let', 
    'null', 
    'return', 
    'switch', 
    'throw', 
    'try', 
    'true', 
    'var', 
    'while']

grammarDict = {}

# Membaca txt
def readGrammarFile(filename):
  with open(filename) as cfg_file:
    baris = cfg_file.readlines()
    barisConverted = []
    for i in range(len(baris)):
      splitBaris = baris[i].replace("->", "").split()
      barisConverted.append(splitBaris)
  return barisConverted

# Menuliskan grammar jadi txt
def grammattotxt(grammar):
    file = open('cnf.txt', 'w')
    for aturan in grammar:
        file.write(aturan[0])
        file.write(" -> ")
        for i in aturan[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()