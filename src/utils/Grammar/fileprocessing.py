
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

#Adding rule to global var
def addGrammarRule(rule):
  global grammarDict
  
  if rule[0] not in grammarDict:
    grammarDict[rule[0]] = []
  grammarDict[rule[0]].append(rule[1:])

def convertGrammar(grammar):
    global grammarDict
    idx = 0
    unitProductions, res = [], []
    for rule in grammar:
      new_rules = []
      # buat yang cuma satu nonterminal/terminal di kanan
      if len(rule) == 2 and not rule[1][0].islower() :
        unitProductions.append(rule)
        addGrammarRule(rule)
        continue
      # Proses if lebih dari 3 nonterminalnya ini bakal di split jadi cuma 3 doang  
      while len(rule) > 3:
        
        new_rules.append([f"{rule[0]}{idx}", rule[1], rule[2]])
        rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
        idx += 1
      if rule:
        addGrammarRule(rule)
        res.append(rule)
      if new_rules:
        for i in range(len(new_rules)):
          res.append(new_rules[i])

    # Proses cuma yang ada 1 non terminal di kanan
    while unitProductions:
      rule = unitProductions.pop() 
      if rule[1] in grammarDict:
        for item in grammarDict[rule[1]]:
          new_rule = [rule[0]] + item
          # nonterminal dikanan bakal dirubah either kalo panjangnya 3 / ada terminal
          if len(new_rule) > 2 or new_rule[1][0].islower():
            res.append(new_rule)
          #Kalo cuma 2 tp dia bukan terminal masukin lg ke production ujungnya bakal dirubah jadi terminal
          else:
            unitProductions.append(new_rule)
          addGrammarRule(new_rule)
    return res

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

grammattotxt(convertGrammar(readGrammarFile('grammar.txt')))