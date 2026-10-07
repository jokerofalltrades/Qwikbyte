from typing import Any

import arithemtic_functions
import input_output
import variable_handling


def identify_function(line_num: int, line: str, vars: dict[str, Any], in_line_exectuion: bool = False):
    operation_result: Any = None
    if line[0] == "=" and not in_line_exectuion:
        key, value = variable_handling.assignment(line_num, line[1:], vars)
        vars[key] = value
    elif line[0] == "+":
        operation_result = arithemtic_functions.addition(line_num, line[1:], vars)
    elif line[0:2] == "()":
        if line[2:5] == "out":
            input_output.out(line_num, line[6:], vars)
        if line[2:7] == "clear":
            variable_handling.clear(line_num, line[8:], vars)
        if line[2:5] == "del":
            variable_handling.delete(line_num, line[6:], vars)

    return operation_result
