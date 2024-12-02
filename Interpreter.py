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
        if piece[comma+1] == "'" and piece[len(comma)] == "'":
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
                varValues.append(int(piece[comma+1:len(piece)]))
            except ValueError:
                try:
                    varValues.append(float(piece[comma+1:len(piece)]))
                except ValueError:
                    print(f"Error Code 4: Error on line {i+1}, variable declaration is missing correct syntax. use ' ' to define a string and a # to define true or false.")
                    sys.exit()
    else:
        print(f"Error Code 2: Error on line {i+1}, missing ',' from variable declaration.")
        sys.exit()

def addition(piece, vars, varValues):
    comma = piece.find(",")
    result = None
    if comma != -1:
        if piece[1:comma] in vars:
            pass
        elif piece[1] == "'":
            if piece[comma+1] == "'" or piece[comma+1:len(piece)] in vars:
                pass
            else:
                print(f"Error Code 7: Error on line {i+1}, cannot add string to other data types. If you are adding to a variable then the varaible does not exist.")
                sys.exit()
        else:
            value1 = 0
            try:
                value1 = int(piece[1:comma])
            except ValueError:
                try:
                    value1 = float(piece[1:comma])
                except ValueError:
                    print(f"Error Code 6: Error on line {i+1}, Invalid data type involved with addition.")
                    sys.exit()
            if piece[comma+1] == "'":
                print(f"Error Code 8: Error on line {i+1}, Strings cannot be added to a number.")
                sys.exit()
            elif piece[comma+1:len(piece)] in vars:
                try:
                    result = varValues[vars.index(piece[comma+1:len(piece)])] + value1
                except TypeError or ValueError:
                    print(f"Error Code 9: Error on line {i+1}, variable value cannot be added to an integer.")
                    sys.exit()
            else:
                value2 = 0
                try:
                    value2 = int(piece[comma+1:len(piece)])
                except ValueError:
                    try:
                        value2 = float(piece[comma+1:len(piece)])
                    except ValueError:
                        print(f"Error Code 6: Error on line {i+1}, Invalid data type involved with addition.")
                        sys.exit()
                result = value1 + value2
                
    else:
        print(f"Error Code 5: Error on line {i+1}, missing ',' from addition.")
        sys.exit()
    if result is None:
        print(f"Error Code 10: Error on line {i+1}. Undefined Error with addition. Please report how you got this error.")
    return result

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
    if type(piece) is not list:
        if piece[0] == "=":
             assignment(piece, vars, varValues)
        elif piece[0] == "+":
            result = addition(piece, vars, varValues)
        elif piece[0:1] == ":=":
            vars, varValues = updateValue(piece, vars, varValues)
    else:
        pass
    print(piece)
print(result)
#print(f"Variables: {vars[0]}, {vars[1]}, {vars[2]}")
#print(f"Variable Values: {varValues[0]}, {varValues[1]}, {varValues[2]}")
