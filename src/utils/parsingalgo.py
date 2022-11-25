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
