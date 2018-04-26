tokens = None
token = None

def globes(tokenlist):
        global tokens
        global token
        
        tokens = tokenlist
        token = tokens[0]
        
def match(expected):
    global token
    global tokens
    if token._kind == expected:
        tokens.pop(0)
        
        if len(tokens) != 0:
            token = tokens[0]
        else:
            print("EMPTY")
        return True
    else:
        print("one expected", expected, ", but got", token._kind)
        print(tokens[0].tostr(),tokens[1].tostr(),tokens[2].tostr(),tokens[3].tostr())
        return False
    
def match2(expected):
    global token
    global tokens
    if token._value == expected:
        tokens.pop(0)
        
        if len(tokens) != 0:
            token = tokens[0]
        return True
    else:
        print("expected", expected, ", but got", token._value)
        print(tokens[0].tostr(),tokens[1].tostr(),tokens[2].tostr(),tokens[3].tostr())
        return False
    
def match3(expected):
    global token
    global tokens
    if expected in token._kind:
        tokens.pop(0)
        
        if len(tokens) != 0:
            token = tokens[0]
        return True
    else:
        print("expected", expected, ", but got", token._kind)
        print(tokens[0].tostr(),tokens[1].tostr(),tokens[2].tostr(),tokens[3].tostr())
        return False

def header():
    return match2("program") and match2(":") and match("VARIABLE") and match2(";") and declarations()

def declarations():
        return match2("var") and match2(":") and idlist() and match2(";")

def idlist():
        return match("VARIABLE") and idlist2()
    
def idlist2():
    global token
    
    if token._value == ",":
        match2(",")
        return idlist()
    #elif token._value == ";":
        #match2(";")
        #return True
    else:
        return True

def body():
    return match2("begin") and match2(":") and statement_list() and match2("halt") and match2(".")

def statement_list():

    if statement():
        return statement_list()
    else:
        return True

def statement():
    global token
    
    if token._kind == "VARIABLE":
        return match("VARIABLE") and match2(":=") and expr() and match2(";")
    elif token._value is "print":
        return match2("print") and match2(":") and match("VARIABLE") and match2(";")
    elif token._value == "if":
        return match2("if") and match2(":") and expr() and match2(",") and match2("then") and match2(":") and statement_list() and match2("end") and match2(".")
    elif token._value is "while":
        return match2("while") and match2(":") and expr() and match2(",") and match2("do") and match2(":") and statement_list() and match2("end") and match2(".")
    else:
        return False

def expr():
    global token
    
    if token._kind == "VARIABLE":
        return match("VARIABLE")
    elif token._kind == "NUMBER":
        return match("NUMBER")
    elif token._kind == "REL_OP":
        return match("REL_OP")
    elif token._kind == "OPEN_PAREN":
        return match("OPEN_PAREN") and expr() and match3("OP") and expr() and match("CLOSE_PAREN")
    else:
        print("error")
        return False

def parse(t):
    globes(t)

    return header() and body()
    