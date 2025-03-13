import math


class QuadraticEquationSolver:
    def __init__(self, a: int, b: int, c: int) -> None:
        self._result = dict()

        self._a = a
        self._b = b
        self._c = c

    def get_result(self) -> dict:
        return self._result

    def resolve(self) -> None:
        discriminator = self._b**2 - 4*self._a*self._c

        if not discriminator:
            x1 = -self._b / (2 * self._a)
            self._result = {"x1": x1}
        elif discriminator > 0:
            x1 = (-self._b + math.sqrt(discriminator)) / (2 * self._a)
            x2 = (-self._b - math.sqrt(discriminator)) / (2 * self._a)

            self._result = {"x1": x1, "x2": x2}
