# Quadratic Equation Solver

Консольна програма для розв’язання квадратних рівнянь виду: ax^2 + bx + c = 0

Підтримується два режими роботи:
- Інтерактивний режим: користувач вводить коефіцієнти вручну.
- Неінтерактивний (файловий) режим: програма отримує шлях до файлу з коефіцієнтами рівняння.

---

## Інструкція до запуску
### Вимоги
- Python 3.10+

### Кроки
1) Клонувати репозиторій <br>
`% git clone https://github.com/Yaroslav702/SDM_Lab_1.git equation_solver` <br>
`% cd equation_solver`
2) Запустити програму в інтерактивному режимі: <br>
`% python3 equation.py`
3) Запустити програму в неінтерактивному режимі: <br>
`% python3 equation.py <шлях_до_файлу>`

---

## Формат файлу
Файл повинен містити три дійсні числа (a, b, c), розділені одним пробілом. <br>
Використовується десятковий роздільник «.» (крапка).

Приклад файлу:
`1.0 5.0 6.0`

⚠️ Файл має закінчуватися символом нового рядка (\n).

---

[Revert commit link](https://github.com/Yaroslav702/SDM_Lab_1/commit/16a58d12484ca1f2b4ce11053a89e4c2e67b8adb)