def quadratic_equation(a: float, b: float, c: float) -> str:

    x1 = (-b + ((b**2 - 4 * a * c) ** 0.5)) / (2 * a)
    x2 = (-b - ((b**2 - 4 * a * c) ** 0.5)) / (2 * a)
    # print(f" x1 = {x1:.2f}, x2 = {x2 :.2f}")

    return f"x1 = {x1:.2f}, x2 = {x2:.2f}"
