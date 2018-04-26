import string
from main import token

KW = ["BEGIN", "DO", "END", "FALSE", "HALT", "IF", "PRINT", "PROGRAM", "THEN", "TRUE", "VAR", "WHILE"]
AROP = ["+", "-", "*", "/", "%"]
ROP = ["=", "!=", "<", "<=", ">", ">="]
AOP = [":="]
PUNC = [":", ";", ".", ","]
OPEN_PAREN = ["("]
CLOSE_PAREN = [")"]
DUAL = [":", "!", "<", ">"]

MASTER = list(KW + AROP + ROP + PUNC + OPEN_PAREN + CLOSE_PAREN)

def _tokenify(chars):
    tokenlist = []

    i = 0;
    while i < len(chars):
        
        if chars[i] in string.ascii_letters:
            word = ""
            while True:
                word += chars[i]
                if chars[i+1] not in string.ascii_letters:
                    break
                else:
                    i += 1
            if word.upper() in KW:
                tokenlist.append(token.Token("KEYWORD", word))
            else:
                tokenlist.append(token.Token("VARIABLE", word))
    
        if chars[i] in string.digits:
            num = ""
            while True:
                num += str(chars[i])
                if chars[i+1] not in string.digits:
                    break
                else:
                    i += 1

            tokenlist.append(token.Token("NUMBER", num))

        if chars[i] in DUAL:
            if chars[i] == "!" and chars[i+1] == "=":
                tokenlist.append(token.Token("REL_OP", "!="))
                i += 2
                continue
            
            if chars[i] == ":" and chars[i+1] == "=":
                tokenlist.append(token.Token("ASSIGN_OP", ":="))
                i += 2
                continue
            elif chars[i] == ":":
                tokenlist.append(token.Token("PUNC", chars[i]))
                i += 1
                continue
                
            if chars[i] == "<" and chars[i+1] == "=":
                tokenlist.append(token.Token("REL_OP", "<="))
                i += 2
                continue
            elif chars[i] == "<":
                tokenlist.append(token.Token("REL_OP", chars[i]))
                i += 1
                continue
            
            if chars[i] == ">" and chars[i+1] == "=":
                tokenlist.append(token.Token("REL_OP", ">="))
                i += 2
                continue
            elif chars[i] == ">":
                tokenlist.append(token.Token("REL_OP", chars[i]))
                i += 1
                continue
                
        if chars[i] in AROP:
            tokenlist.append(token.Token("ARITH_OP", chars[i]))
            i += 1
            continue
        if chars[i] in ROP:
            tokenlist.append(token.Token("REL_OP", chars[i]))
            i += 1
            continue
        if chars[i] in PUNC and chars[i] not in DUAL:
            tokenlist.append(token.Token("PUNC", chars[i]))
            i += 1
            continue
        if chars[i] in OPEN_PAREN:
            tokenlist.append(token.Token("OPEN_PAREN", chars[i]))
            i += 1
            continue
        if chars[i] in CLOSE_PAREN:
            tokenlist.append(token.Token("CLOSE_PAREN", chars[i]))
            i += 1
            continue
        
        i += 1 
    tokenlist.append(token.Token("EOF", "$"))
    
    for i in range(0, len(tokenlist)):
        tokenlist[i].tostr()
    
    return tokenlist

def scanner(filename):
    commentstate = False
    chars = []

    with open(filename) as f:
        for line in f:
            for ch in line:
                if ch in string.whitespace:
                    continue
                if ch == "#":
                    commentstate = not commentstate
                    continue

                if commentstate == True:
                    continue
                elif ch in MASTER or ch in string.ascii_letters or ch in string.digits or ch in "!":
                    chars.append(ch)
                else:
                    print("Error: got symbol " + ch)
                    return False

    return(_tokenify(chars))
