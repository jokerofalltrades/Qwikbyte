import sys

vars = []
varValues = []
tempCodeStorage = []

def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def assignment(piece, vars, varValues):
    comma = piece.find(",")
    if comma != -1:
        if str(piece[1:comma]) not in vars:
            vars.append(str(piece[1:comma]))
        else:
            print(f"Error Code 1: Error on line {i+1}, already defined variable being redefined.")
            sys.exit()
        if piece[comma+1] == "'":
            varValues.append(piece[comma+2:find_nth_overlapping(piece,"'",2)])
        elif piece[comma+1] == "#":
            if piece[comma+2:len(piece)] == "1":
                varValues.append("True")
            elif piece[comma+2:len(piece)] == "0":
                varValues.append("False")
            else:
                print(f"Error Code 3: Error on line {i+1}, When assigning variables '#' is used to denote a true or false value. '0' is false and '1' is true.")
                sys.exit()
        else:
            try:
                if int(piece[comma+1:len(piece)]) == float(piece[comma+1:len(piece)]):
                    varValues.append(int(piece[comma+1:len(piece)]))
                else:
                    varValues.append(float(piece[comma+1:len(piece)]))
            except ValueError:
                print(f"Error Code 4: Error on line {i+1}, variable declaration is missing correct syntax. use ' ' to define a string and a # to define true or false.")
    else:
        print(f"Error Code 2: Error on line {i+1}, missing ',' from variable declaration.")
        sys.exit()

inputcode = input("Please input the qwikbyte code: ")
code = inputcode.split(";")
for i, piece in enumerate(code):
    code[i] = ("".join(piece.split()))
code.pop()

for i, piece in enumerate(code):
    tempCodeStorage = []
    if "[" in piece or "{" in piece:
        if "[" in piece and "{" in piece:
            tempCodeStorage = piece.split("[")
            for e, subpiece in enumerate(tempCodeStorage):
                    tempCodeStorage[e] = "".join(subpiece.split("{"))
        else:
            if "{" in piece:
                tempCodeStorage = piece.split("{")
            if "[" in piece:
                tempCodeStorage = piece.split("[")
        for v, subpiece in enumerate(tempCodeStorage):
            tempCodeStorage[v] = subpiece.replace("]","")
            tempCodeStorage[v] = subpiece.replace("}","")
        code[i] = tempCodeStorage
    
        
for i, piece in enumerate(code):
    if piece[0] == "=":
        assignment(piece, vars, varValues)
    elif piece[0] == "+":
        pass
    print(piece)
print(f"Variables: {vars[0]}, {vars[1]}, {vars[2]}")
print(f"Variable Values: {varValues[0]}, {varValues[1]}, {varValues[2]}")
