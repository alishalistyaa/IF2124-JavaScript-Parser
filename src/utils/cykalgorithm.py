
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
        for producer, productions in grammarDictionary.items(): #R.Items berfungsi untuk memanggil semua pasangan key-value yang ada di dictionary grammar, traversal untuk setiap grammar
            for production in productions: # traversal untuk setiap value yang dimiliki satu key
                if len(production) == 1 and production[0] == inputCodeLength[j]: #Jika producer menghasilkan terminal, karena harus menghasilkan terminal
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
      
