from typing import Any

import code_handling
import error_handling


def assignment(line_num: int, line: str, vars: dict[Any, Any]) -> tuple[str, Any]:
    comma_location: int = line.find(",")
    if comma_location == -1:
        error_handling.call_error(1, line_num, "missing ',' from assignment")

    var_name = line[:comma_location].strip()
    var_value = parse_var_value(line[comma_location+1:].strip(), line_num, vars)

    if var_name in vars:
        error_handling.raise_error(4, line_num, "variable already exists. Use @= to update the value")

    if var_value is None:
        error_handling.raise_error(5, line_num, "variable declaration is missing correct syntax. use ' ' to define a string and a # to define true or false")

    return var_name, var_value

def parse_var_value(var_value: Any, line_num: int, vars: dict[Any, Any]) -> Any:
    if var_value[0] == "(" and var_value[-1] == ")":
        return code_handling.identify_function(line_num, var_value[1:-1], vars, in_line_exectuion=True)
    elif var_value[0] == "'" and var_value[-1] == "'":
        return var_value.replace("'", "")
    elif var_value[0] == "#":
        return (True if var_value[1] == "1" else False if var_value[1] == "0" else None)
    elif var_value[0] == "[" and var_value[-1] == "]":
        return [parse_var_value(item.strip(), line_num, vars) for item in var_value[1:-1].split(",")]
    else:
        try:
            return int(var_value)
        except (TypeError, ValueError):
            try:
                return float(var_value)
            except (TypeError, ValueError):
                return None

def clear(line_num: int, line: str, vars: dict[Any, Any]) -> None:
    if line not in vars:
        error_handling.raise_error(6, line_num, "variable does not exist so cannot be cleared")
    vars[line] = None

def delete(line_num: int, line: str, vars: dict[Any, Any]):
    if line not in vars:
        error_handling.raise_error(7, line_num, "variable does not exist so cannot be deleted")
    vars.pop(line)
