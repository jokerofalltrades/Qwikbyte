from typing import Any

import code_handling


def out(line_num: int, to_output: str, vars: dict[Any, Any]):
    if to_output[0] == "(" and to_output[-1] == ")":
        to_output = code_handling.identify_function(line_num, to_output[1:-1], vars, in_line_exectuion=True)
    if to_output in vars:
        to_output = vars[to_output]

    print(to_output)