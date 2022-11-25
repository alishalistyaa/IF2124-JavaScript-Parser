
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

# Konversi CFG to CNF
def convertGrammar(grammar):
  global grammarDict
  idx = 0
  checkUnitProd = []
  res = []
  
  # Mengecek grammar
  for aturan in grammar:
      new_aturan = []
      # STEP 1: Eliminasi Unit Productions
      if len(aturan) == 2 and not aturan[1][0].islower() :
          checkUnitProd.append(aturan)
          # Masukkan ke dalam aturan baru
          if aturan[0] not in grammarDict:
            grammarDict[aturan[0]] = []
          grammarDict[aturan[0]].append(aturan[1:])
          continue

      # Eliminasi jika menghasilkan variabel lebih dari 3  
      while len(aturan) > 3:
        new_aturan.append([f"{aturan[0]}{idx}", aturan[1], aturan[2]])
        aturan = [aturan[0]] + [f"{aturan[0]}{idx}"] + aturan[3:]
        idx += 1

      if aturan:
        # Masukkan ke dalam aturan baru
        if aturan[0] not in grammarDict:
            grammarDict[aturan[0]] = []
        grammarDict[aturan[0]].append(aturan[1:])
        res.append(aturan)

      if new_aturan:
          for i in range(len(new_aturan)):
              res.append(new_aturan[i])

  # Eliminasi Unit Productions
  while checkUnitProd:
    print("hello")
    aturan = checkUnitProd.pop() 
    if aturan[1] in grammarDict:
        for item in grammarDict[aturan[1]]:
            
            aturan_prod = [aturan[0]] + item
            # nonterminal dikanan bakal dirubah either kalo panjangnya 3 / ada terminal
            if len(aturan_prod) > 2 or aturan_prod[1][0].islower():
              res.append(aturan_prod)
            #Kalo cuma 2 tp dia bukan terminal masukin lg ke production ujungnya bakal dirubah jadi terminal
            else:
              checkUnitProd.append(aturan_prod)
            # Masukkan ke grammar baru
            if aturan[0] not in grammarDict:
                grammarDict[aturan[0]] = []
            grammarDict[aturan[0]].append(aturan[1:])
  return res

# Menuliskan grammar jadi txt
def grammattotxt(grammar):
    file = open('cnf.txt', 'w')
    for aturan in grammar:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

grammattotxt(convertGrammar(readGrammarFile('gare.txt')))