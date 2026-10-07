from typing import Any

import code_handling

vars: dict[str, Any] = {}

try:
    with open("main.qkb") as code:
        inputcode = code.read().strip()
except FileNotFoundError:
    inputcode = input("Please input the qwikbyte code: ")

code = inputcode.split(";")
code.pop()

for i, piece in enumerate(code):
    #if type(piece) is not list:
    result = code_handling.identify_function(i+1, piece.strip(), vars)
    #else:
        #for e, subpiece in enumerate(piece):
            #if subpiece[0:1] == ":=":
                #pass
    print(piece.strip())
    print(vars)
#print(f"Variables: {vars[0]}, {vars[1]}, {vars[2]}")
#print(f"Variable Values: {varValues[0]}, {varValues[1]}, {varValues[2]}")
