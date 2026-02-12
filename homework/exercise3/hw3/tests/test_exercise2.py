from solution.exercise2 import fibonacci


def test_febonacci1() -> None:
    result = fibonacci(5)
    assert result == 5


def test_febonacci2() -> None:
    result = fibonacci(57)
    assert result == 365435296162


def test_febonacci3() -> None:
    result = fibonacci(200)
    assert result == 280571172992510140037611932413038677189525


def test_febonacci4() -> None:
    result = fibonacci(260)
    assert result == 971183874599339129547649988289594072811608739584170445


def test_febonacci5() -> None:
    result = fibonacci(500)
    expected = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
    assert result == expected
