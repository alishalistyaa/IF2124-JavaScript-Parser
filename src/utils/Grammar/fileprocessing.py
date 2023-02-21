# CFG TO CNF CONVERTER
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
  # Membuka file
  with open(filename) as cfg_file:
    baris = cfg_file.readlines()
    barisConverted = []
    for i in range(len(baris)):
      splitBaris = baris[i].replace("->", "").split()
      barisConverted.append(splitBaris)
  return barisConverted

def convertGrammar(grammar):
  global grammarDict
  idx = 0
  checkUnitProd = [] 
  result = []

  # Parsing aturan di dalam grammar
  for aturan in grammar:
    new_rules = []
    # RULE 1: Catat Unit Production / Lebih dair satu terminal
    if len(aturan) == 2 and not aturan[1][0].islower() :
      checkUnitProd.append(aturan)
      if aturan[0] not in grammarDict:
        grammarDict[aturan[0]] = []
      grammarDict[aturan[0]].append(aturan[1:])
      continue
    

    # RULE 1.5 : Split variabel produksi lebih dari 3
    while len(aturan) > 3:
      
      new_rules.append([f"{aturan[0]}{idx}", aturan[1], aturan[2]])
      aturan = [aturan[0]] + [f"{aturan[0]}{idx}"] + aturan[3:]
      idx += 1
    if aturan:
      if aturan[0] not in grammarDict:
        grammarDict[aturan[0]] = []
      grammarDict[aturan[0]].append(aturan[1:])
      result.append(aturan)
    if new_rules:
      for i in range(len(new_rules)):
        result.append(new_rules[i])

  # Rule 2: Eliminasi Unit Production
  # Checking apakah ada pada unit production
  while checkUnitProd:
    # Mengolah satu per satu unit production
    aturan = checkUnitProd.pop() 
    if aturan[1] in grammarDict:
      for item in grammarDict[aturan[1]]:
        new_rule = [aturan[0]] + item
        # Menyiapkan variabel baru
        if len(new_rule) > 2 or new_rule[1][0].islower():
          result.append(new_rule)
        else:
          checkUnitProd.append(new_rule)
        if aturan[0] not in grammarDict:
          grammarDict[aturan[0]] = []
        grammarDict[aturan[0]].append(aturan[1:])
  return result

# Menuliskan grammar jadi txt
def grammartotxt(grammar):
    file = open('cnf.txt', 'w')
    for aturan in grammar:
        file.write(aturan[0])
        file.write(" -> ")
        for i in aturan[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()