import sys
import os
import re
from utils import QuadraticEquationSolver


def get_float_input(prompt: str, allow_zero: bool = True):
    while True:
        try:
            value = float(input(prompt))
            if not allow_zero and value == 0:
                print("Error: 'a' cannot be zero.")
                continue
            return value
        except ValueError:
            print("Error: Expected a valid real number, got invalid instead.")


def output_result(result_dict: dict) -> None:
    print(f"There are {len(result_dict)} roots.")

    for key, value in result_dict.items():
        print(f"{key} = {value}")


def resolve_interactive() -> None:
    a = get_float_input("a = ", False)
    b = get_float_input("b = ")
    c = get_float_input("c = ")

    solver = QuadraticEquationSolver(a, b, c)
    solver.resolve()

    solver.set_prefix()
    output_result(solver.get_result())


def resolve_file_mode(file_path: str) -> None:
    if not os.path.exists(file_path):
        raise Exception(f"file {file_path} does not exist")

    with open(file_path, 'r') as file:
        content = file.read().strip()
        if not re.fullmatch(r"-?\d+\.\d*\s-?\d+\.\d*\s-?\d+\.\d*", content):
            raise ValueError("Invalid file format")

        a, b, c = map(float, content.split())

        if a == 0:
            raise Exception("Error: 'a' cannot be zero.")

        solver = QuadraticEquationSolver(a, b, c)
        solver.resolve()

        solver.set_prefix()
        output_result(solver.get_result())


def main() -> None:
    match len(sys.argv):
        case 2:  # non-interactive method
            resolve_file_mode(sys.argv[1])
        case 1:  # interactive method
            resolve_interactive()
        case _:
            raise Exception("Unexpected argument.")


if __name__ == "__main__":
    main()
