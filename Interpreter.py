vars = []
varvalues = []


def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

inputcode = input("Please input the qwikbyte code: ")
code = inputcode.split(";")
for i, piece in enumerate(code):
    code[i] = ("".join(piece.split()))
code.pop()
for i, piece in enumerate(code):
    if piece[0] == "=":
        comma = piece.find(",")
        if comma != -1:
            if str(piece[1:comma]) not in vars:
                vars.append(str(piece[1:comma]))
            else:
                print(f"Error Code 1: Error on line {i+1}, already defined variable being redefined.")
                exit()
            if piece[comma+1] == "'":
                varvalues.append(piece[comma+2:find_nth_overlapping(piece,"'",2)])
            elif piece[comma+1] == "#":
                if piece[comma+2:len(piece)] == "1":
                    varvalues.append("True")
                elif piece[comma+2:len(piece)] == "0":
                    varvalues.append("False")
                else:
                    print(f"Error Code 3: Error on line {i+1}, When assigning variables '#' is used to denote a true or false value. '0' is false and '1' is true.")
                    exit()
            else:
                print("something went wrong")
        else:
            print(f"Error Code 2: Error on line {i+1}, missing ',' from variable declaration.")
            exit()
    print(piece)
    print(vars[0])
    print(varvalues[0])
