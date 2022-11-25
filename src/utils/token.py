import re

# Untuk mengimplementasikan FA untuk variabel dan operator, digunakan RegEx
listToken = [
    # Operator
    
    # INC DEC -> UNARY
    (r'\+\+', "INCR"),
    (r'\-\-', "DECR"),
    
    # UNARY
    (r'~', "BNOT"),
    (r'!', "LNOT"),
    
    # ARITH -> BINARY OP 
    (r'\+(?!\=)', "ADD"), # biner, kalo uner jadi conversion
    (r'\-(?!\=)', "SUB"), # biner, kalo uner jadi conversion
    (r'/(?!\=)', "DIV"),
    (r'\*(?!\=)', "MUL"),
    (r'\%(?!\=)', "REM"),
    (r'\*\*(?!\=)', "EXP"),

    # RELATIONAL -> BINARY OP
    (r'in', "IN"),
    (r'instanceof', "INSOF"),
    (r'<(?!\=)', "L"),
    (r'>(?!\=)', "G"),
    (r'<=', "LE"),
    (r'>=', "GE"),

    # EQUALITY -> BINARY OP
    (r'==(?!\=)', "EQ"),
    (r'!=(?!\=)', "INEQ"),
    (r'===', "SEQ"),
    (r'!==', "SINEQ"),

    # BITWISE SHIFT -> BINARY OP
    (r'<<', "LS"),
    (r'>>(?!\>)', "RS"),
    (r'>>>', "URS"),

    # BINARY BITWISE -> BINARY OP
    (r'&(?!\=)', "BAND"),
    (r'\|(?!\=)', "BOR"),
    (r'\^(?!\=)', "BXOR"),

    # BINARY LOGICAL -> BINARY OP
    (r'&&(?!\=)', "LAND"),
    (r'\|\|(?!\=)', "LOR"),
    (r'\?\?', "NCO"),

    # ASSIGNMENT -> BINARY OP
    (r'=', "A"),
    (r'\*=', "MULA"),
    (r'/=', "DIVA"),
    (r'%=', "REMA"),
    (r'\+=', "ADDA"),
    (r'-=', "SUBA"),
    (r'<<=', "LSA"),
    (r'>>=', "RSA"),
    (r'>>>=', "URSA"),
    (r'&=', "BANDA"),
    (r'\^=', "BXORA"),
    (r'\|=', "BORA"),
    (r'&&=', "LANDA"),
    (r'\|\|=', "LORA"),
    
    # LAIN LAIN
    (r'\?', "QUESTM"),
    (r'\:', "COLON"),
    (r'\;', "SCOLON"),
    (r'\.', "DOT"),
    (r'\,', "COMMA"),
    
    # KURUNG
    (r'\[', "KSO"),
    (r'\]', "KSC"),
    (r'\(', "KLO"),
    (r'\)', "KLC"),
    (r'\{', "KKO"),
    (r'\}', "KKC"),
    
    # KEYWORDS
    
    (r'\bconst\b', "CONST"),
    (r'\bvar\b', "VAR"),
    (r'\blet\b', "LET"),
    
    (r'\bif\b', "IF"),
    (r'\belse\b', "ELSE"),
    
    (r'\bswitch\b', "SWITCH"),
    (r'\bcase\b', "CASE"),
    (r'\bdefault\b', "DEFAULT"),
    
    (r'\bwhile\b', "WHILE"),
    (r'\bfor\b', "FOR"),
    (r'\bbreak\b', "BREAK"),
    (r'\bcontinue\b', "CONTINUE"),
    
    (r'\btry\b', "TRY"),
    (r'\bcatch\b', "CATCH"),
    
    (r'\btrue\b', "TRUE"),
    (r'\bfalse\b', "FALSE"),
    
    (r'\bfunction\b', "FUNCTION"),
    (r'\breturn\b', "RETURN"),
    
    (r'\bdelete\b', "DELETE"),
    (r'\bfinally\b', "FINALLY"),
    (r'\bthrow\b', "THROW"),
    (r'\bnull\b', "NULL"),
    
    # Others
    
    # TABS & NEWLINE
    (r'\n', "NEWLINE"),
    (r'[ \t]+', None), # tabs & indent diignore
    
    # COMMENTS
    (r'//[^\n]*', None), # comment sebaris, ignore
    (r'[\n]+[ \t]*/\*[(?!(\"\"\"))\w\W]*\*\\', None), # comment multiline, ignore
    
    # VARIABLE NAME
    (r'[A-Za-z_\$][A-Za-z0-9_\$]*', "VARNAME")
]

def compileAllPattern(listToken):
    for i in range(len(listToken)):
        rStr, nama = listToken[i]
        listToken[i] = (re.compile(rStr),nama)
    return listToken

listRegex = compileAllPattern(listToken)

def createTextTokens(filename):
    # Membaca keseluruhan file
    file = open(filename, 'r', encoding='utf8')
    text = file.read()
    file.close()
    
    # buat tokens
    tokens = []
    foundAll = True
    errorInfo = ("", -1, -1) # kalo bagian angkanya bukan > 0 berarti ada syntax error
    textIdx = 0
    baris = 1
    kolom = 1
    
    while (textIdx < len(text) and foundAll):
        print(textIdx)
        # restart tiap newline
        if text[textIdx] == '\n':
            baris += 1
            kolom = 1

        found = False
        i = 0
        while not(found) and i < len(listRegex):
            regEx, nama = listRegex[i]    

            match = regEx.match(text, textIdx)
            if (match):
                found = True
                if (nama):
                    tokens.append(nama)
            else:
                i += 1

        if (not(found)):
            foundAll = False
            errorInfo = (text[textIdx],baris,kolom)
        else:
            textIdx = match.end(0)
            
        kolom += 1
    
    return tokens, errorInfo