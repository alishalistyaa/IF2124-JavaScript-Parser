def parsingCYK(inputCode, grammarDictionary):
    # I.S. inputCode dan grammarDictionary terdefinisi dan valid
    # F.S. menampilkan Accepted pada terminal jika input code sesuai grammar    
    #      menampilkan Not Accepted jika tidak

    # Mengambil Panjang string kode masukan 
    inputCodeLength = len(inputCode)

    # Menginisialisasi matriks berukuran inputCodeLength x inputCodeLength dengan nilai Nil = ''
    CYKTable = [[[] for j in range(inputCodeLength)] for i in range(inputCodeLength)]

    # Pemrosesan secara traversal per karakter input
    for j in range(0, inputCodeLength):
        for producer, productions in grammarDictionary.items(): #grammarDictionary.Items berfungsi untuk memanggil semua pasangan key-value yang ada di dictionary grammar, traversal untuk setiap grammar
            for production in productions: # traversal untuk setiap value yang dimiliki satu key
                if len(production) == 1 and production[0] == inputCode[j]: #Jika producer menghasilkan terminal, karena harus menghasilkan terminal
                    if not producer in CYKTable[j][j]: #Jika belum ada di CYKTable, masukkan ke CYKTable
                        CYKTable[j][j].append(producer)

        # berfungsi untuk mengisi R bertingkat
        idxrow = j
        while idxrow >= 0:  # untuk setiap row pada CYKTabel yang berada di atas index (j,j)
            for i in range(idxrow, j):  # traversal ke kiri dan ke bawah untuk memeriksa semua kemungkinan
                for producer, productions in grammarDictionary.items():
                    for production in productions: # traversal untuk setiap value yang dimiliki satu key
                        if len(production) == 2 and production[0] in CYKTable[idxrow][i] and production[1] in CYKTable[i + 1][j]: #Jika producer menghasilkan non terminal CNF dan pemeriksaan urutan
                            if not producer in CYKTable[idxrow][j]: #Jika belum ada di CYKTable, masukkan ke CYKTable
                                CYKTable[idxrow][j].append(producer)
            idxrow -= 1
  
    # Grammar yang benar apabila terdapat S pada kotak CYKTabel paling puncak
    if 'Dict' in T[0][inputCodeLength-1]:
        print("Accepted")
    else:
        print("Not Accepted")
      

def convertGrammar(grammar):
  global grammarDict
  idx = 0
  unitProductions, res = [], []
  for rule in grammar:
    new_rules = []
    # buat yang cuma satu nonterminal/terminal di kanan
    if len(rule) == 2 and not rule[1][0].islower() :
      unitProductions.append(rule)
      if rule[0] not in grammarDict:
        grammarDict[rule[0]] = []
      grammarDict[rule[0]].append(rule[1:])
      continue
    # Proses if lebih dari 3 nonterminalnya ini bakal di split jadi cuma 3 doang  
    while len(rule) > 3:
      new_rules.append([f"{rule[0]}{idx}", rule[1], rule[2]])
      rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
      idx += 1
    if rule:
      if rule[0] not in grammarDict:
        grammarDict[rule[0]] = []
      grammarDict[rule[0]].append(rule[1:])
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
        if rule[0] not in grammarDict:
          grammarDict[rule[0]] = []
        grammarDict[rule[0]].append(rule[1:])
  return res

def makeDictionary(grammar):
  dict = {}
  for aturan in grammar :
    dict[str(aturan[0])] = []
  for aturan in grammar :
    elm = []
    for idxRule in range(1, len(aturan)) :
      apd = aturan[idxRule]
      elm.append(apd)
    dict[str(aturan[0])].append(elm)
  return dict