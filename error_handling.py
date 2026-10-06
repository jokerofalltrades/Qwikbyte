import sys


def raise_error(error_code: int, line_num: int, error_info: str):
    print(f"Error code {error_code}: Error on line {line_num}, {error_info}.")
    sys.exit()