from typing import Any

import error_handling


def addition(line_num: int, line: str, vars: dict[Any, Any]) -> int | str | float | list[Any]:
    comma_location: int = line.find(",")
    if comma_location == -1:
        error_handling.raise_error(1, line_num, "missing ',' from addition")

    addend_1 = parse_addend(line[:comma_location], vars)
    addend_2 = parse_addend(line[comma_location+1:], vars)

    both_numeric = isinstance(addend_1, (int, float)) and isinstance(addend_2, (int, float))
    same_type = type(addend_1) is type(addend_2)
    if not (both_numeric or same_type):
        error_handling.raise_error(2, line_num, "variable type mismatch in addition")

    try:
        result = addend_1 + addend_2
    except (TypeError, ValueError):
        error_handling.raise_error(3, line_num, "unknown error with addition, please report how you got this")

    return result

def parse_addend(addend: Any, vars: dict[Any, Any]) -> Any:
    if addend in vars:
        addend = vars[addend]

    if not isinstance(addend, str):
        return addend

    try:
        return int(addend)
    except (TypeError, ValueError):
        try:
            return float(addend)
        except (TypeError, ValueError):
            return addend.strip().replace("'", "")
