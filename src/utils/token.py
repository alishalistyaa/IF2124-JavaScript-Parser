import re

# Untuk mengimplementasikan FA untuk variabel dan operator, digunakan RegEx
listToken = [
    # Others
    
    # TABS & NEWLINE
    (r'\n', "newline"),
    (r'[ \t]+', None), # tabs & indent diignore
    
    # COMMENTS
    (r'//[^\n]*', None), # comment sebaris, ignore
    (r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/', None), # comment multiline, ignore
    
    # Operator
    
    # INC DEC -> UNARY
    (r'\+\+', "incr"),
    (r'\-\-', "decr"),

    # EQUALITY -> BINARY OP
    (r'===', "seq"),
    (r'!==', "sineq"),
    (r'==', "eq"),
    (r'!=', "ineq"),

    # UNARY
    (r'~', "bnot"),
    (r'!', "lnot"),

    # ASSIGNMENT -> BINARY OP
    (r'\*\*=', "expna"),
    (r'\*=', "mula"),
    (r'/=', "diva"),
    (r'%=', "rema"),
    (r'\+=', "adda"),
    (r'-=', "suba"),
    (r'<<=', "lsa"),
    (r'>>>=', "ursa"),
    (r'>>=', "rsa"),
    (r'&&=', "landa"),
    (r'\|\|=', "lora"),
    (r'&=', "banda"),
    (r'\^=', "bxora"),
    (r'\|=', "bora"),
    
    # RELATIONAL BINARY
    (r'<=', "le"),
    (r'>=', "ge"),

    # ARITH -> BINARY OP
    (r'\+', "add"), # biner, kalo uner jadi conversion
    (r'\-', "sub"), # biner, kalo uner jadi conversion
    (r'/', "div"),
    (r'\*\*', "expn"),
    (r'\*', "mul"),
    (r'\%', "rem"),

    # BITWISE SHIFT -> BINARY OP DONE
    (r'<<', "ls"),
    (r'>>>', "urs"),
    (r'>>', "rs"),

    # RELATIONAL -> BINARY OP
    (r'<', "l"),
    (r'>', "g"),

    # BINARY LOGICAL -> BINARY OP
    (r'&&', "land"),
    (r'\|\|', "lor"),

    # BINARY BITWISE -> BINARY OP
    (r'&', "band"),
    (r'\|', "bor"),
    (r'\^', "bxor"),

    # ASSIGNMENT BINARY
    (r'=', "a"),
    
    # LAIN LAIN
    (r'\?', "questm"),
    (r'\:', "colon"),
    (r'\;', "scolon"),
    (r'\.', "dot"),
    (r'\,', "comma"),
    
    # KURUNG
    (r'\[', "kso"),
    (r'\]', "ksc"),
    (r'\(', "klo"),
    (r'\)', "klc"),
    (r'\{', "kko"),
    (r'\}', "kkc"),
    
    # KEYWORDS
    
    (r'\bconst\b', "const"),
    (r'\bvar\b', "var"),
    (r'\blet\b', "let"),
    
    (r'\bif\b', "if"),
    (r'\belse\b', "else"),
    
    (r'\bswitch\b', "switch"),
    (r'\bcase\b', "case"),
    (r'\bdefault\b', "default"),
    
    (r'\bdo\b', "do"),
    (r'\bwhile\b', "while"),
    (r'\bfor\b', "for"),
    (r'\bbreak\b', "break"),
    (r'\bcontinue\b', "continue"),
    
    (r'\btry\b', "try"),
    (r'\bcatch\b', "catch"),
    
    (r'\btrue\b', "true"),
    (r'\bfalse\b', "false"),
    
    (r'\bfunction\b', "function"),
    (r'\breturn\b', "return"),
    
    (r'\bdelete\b', "delete"),
    (r'\bfinally\b', "finally"),
    (r'\bthrow\b', "throw"),
    (r'\bnew\b', "new"),
    (r'\bnull\b', "null"),

    # TYPES
    (r'[\+\-]?[0-9]*\.[0-9]+', "num"),
    (r'[\+\-]?[1-9][0-9]+', "num"),
    (r'[\+\-]?[0-9]', "num"),
    (r'\"[^\"\n]*\"', "str"),
    (r'\'[^\'\n]*\'', "str"),
    (r'\`[^\'\n]*\`', "str"),
    (r'\`[(?!(\`))\w\W]*\`', "mlstr"),

    # IDENTIFIER
    (r'[A-Za-z_\$][A-Za-z0-9_\$]*', "iden")
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