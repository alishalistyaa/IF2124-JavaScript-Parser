import re

# Untuk mengimplementasikan FA untuk variabel dan operator, digunakan RegEx
listToken = [
    # Others
    
    # TABS & NEWLINE
    (r'\n', "NEWLINE"),
    (r'[ \t]+', None), # tabs & indent diignore
    
    # COMMENTS
    (r'//[^\n]*', None), # comment sebaris, ignore
    (r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/', None), # comment multiline, ignore
    
    # Operator
    
    # INC DEC -> UNARY
    (r'\+\+', "INCR"),
    (r'\-\-', "DECR"),

    # EQUALITY -> BINARY OP
    (r'===', "SEQ"),
    (r'!==', "SINEQ"),
    (r'==', "EQ"),
    (r'!=', "INEQ"),

    # UNARY
    (r'~', "BNOT"),
    (r'!', "LNOT"),

    # ASSIGNMENT -> BINARY OP
    (r'\*\*=', "EXPNA"),
    (r'\*=', "MULA"),
    (r'/=', "DIVA"),
    (r'%=', "REMA"),
    (r'\+=', "ADDA"),
    (r'-=', "SUBA"),
    (r'<<=', "LSA"),
    (r'>>>=', "URSA"),
    (r'>>=', "RSA"),
    (r'&&=', "LANDA"),
    (r'\|\|=', "LORA"),
    (r'&=', "BANDA"),
    (r'\^=', "BXORA"),
    (r'\|=', "BORA"),
    
    # RELATIONAL BINARY
    (r'<=', "LE"),
    (r'>=', "GE"),

    # ARITH -> BINARY OP
    (r'\+', "ADD"), # biner, kalo uner jadi conversion
    (r'\-', "SUB"), # biner, kalo uner jadi conversion
    (r'/', "DIV"),
    (r'\*\*', "EXPN"),
    (r'\*', "MUL"),
    (r'\%', "REM"),

    # BITWISE SHIFT -> BINARY OP DONE
    (r'<<', "LS"),
    (r'>>>', "URS"),
    (r'>>', "RS"),

    # RELATIONAL -> BINARY OP
    (r'<', "L"),
    (r'>', "G"),

    # BINARY LOGICAL -> BINARY OP
    (r'&&', "LAND"),
    (r'\|\|', "LOR"),

    # BINARY BITWISE -> BINARY OP
    (r'&', "BAND"),
    (r'\|', "BOR"),
    (r'\^', "BXOR"),

    # ASSIGNMENT BINARY
    (r'=', "A"),
    
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
    
    (r'\bdo\b', "DO"),
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
    (r'\bnew\b', "NEW"),
    (r'\bnull\b', "NULL"),

    # TYPES
    (r'[\+\-]?[0-9]*\.[0-9]+', "NUM"),
    (r'[\+\-]?[1-9][0-9]+', "NUM"),
    (r'[\+\-]?[0-9]', "NUM"),
    (r'\"[^\"\n]*\"', "STR"),
    (r'\'[^\'\n]*\'', "STR"),
    (r'\`[^\'\n]*\`', "STR"),
    (r'\`[(?!(\`))\w\W]*\`', "MLSTR"),

    # IDENTIFIER
    (r'[A-Za-z_\$][A-Za-z0-9_\$]*', "IDEN")
]

def compileAllPattern(listToken):
    for i in range(len(listToken)):
        rStr, nama = listToken[i]
        listToken[i] = (re.compile(rStr),nama)
    return listToken

listRegex = compileAllPattern(listToken)

def getTokens(filename):
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