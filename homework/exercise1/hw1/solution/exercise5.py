def quadratic_equation(
    coefficient_a: float, coefficient_b: float, coefficient_c: float
) -> str:

    discriminant = coefficient_b**2 - 4 * coefficient_a * coefficient_c
    sqrt_discriminant = discriminant**0.5
    denominator = 2 * coefficient_a

    x1 = (-coefficient_b + sqrt_discriminant) / denominator
    x2 = (-coefficient_b - sqrt_discriminant) / denominator

    return f"x1 = {x1:.2f}, x2 = {x2:.2f}"
