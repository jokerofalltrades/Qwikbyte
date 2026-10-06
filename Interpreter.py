from typing import Any

import arithemtic_functions
import variable_handling

vars: dict[str, Any] = {}
tempCodeStorage = []

def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def bracketsRemove(code):
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
                tempCodeStorage[v] = tempCodeStorage[v].replace("}","")
            tempCodeStorage[:] = [subpiece for subpiece in tempCodeStorage if subpiece != ""]
            code[i] = tempCodeStorage

def updateValue(piece, vars, varValues):
    pass

def identifyFuncToRun(piece, vars, line_num):
    additionUsed = 0
    if piece[0] == "=":
        key, value = variable_handling.assignment(line_num, piece[1:], vars)
        vars[key] = value
    elif piece[0] == "+":
        addresult = arithemtic_functions.addition(line_num, piece[1:], vars)
        additionUsed = 1
    elif piece[0:1] == ":=":
        #vars, varValues = updateValue(piece, vars, varValues)
        pass
    if additionUsed == 1:
        return addresult
    else:
        return None

inputcode = input("Please input the qwikbyte code: ")
code = inputcode.split(";")
code.pop()

for i, piece in enumerate(code):
    #if type(piece) is not list:
    addresult = identifyFuncToRun(piece.strip(), vars, i+1)
    #else:
        #for e, subpiece in enumerate(piece):
            #if subpiece[0:1] == ":=":
                #pass
    print(piece.strip())
    print(addresult)
    print(vars)
#print(f"Variables: {vars[0]}, {vars[1]}, {vars[2]}")
#print(f"Variable Values: {varValues[0]}, {varValues[1]}, {varValues[2]}")
