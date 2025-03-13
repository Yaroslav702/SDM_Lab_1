import math


class QuadraticEquationSolver:
    def __init__(self, a: float, b: float, c: float) -> None:
        self._result = dict()

        self._a = a
        self._b = b
        self._c = c

    def get_result(self) -> dict:
        return self._result

    def set_prefix(self) -> None:
        print(f"Equation is: ({self._a}) x^2 + ({self._b}) x + ({self._c}) = 0")

    def resolve(self) -> None:
        discriminator = self._b**2 - 4*self._a*self._c

        if not discriminator:
            x1 = -self._b / (2 * self._a)
            self._result = {"x1": x1}
        elif discriminator > 0:
            x1 = (-self._b + math.sqrt(discriminator)) / (2 * self._a)
            x2 = (-self._b - math.sqrt(discriminator)) / (2 * self._a)

            self._result = {"x1": x1, "x2": x2}
