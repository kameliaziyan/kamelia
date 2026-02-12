from solution.exercise2 import Calculator
from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch



def test_calculator_add(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    inputs = iter(["add 2 to 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Calculator()

    captured = capsys.readouterr()
    assert "The answer is 7" in captured.out


def test_calculator_invalid_operation(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(["power 2 to 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Calculator()

    captured = capsys.readouterr()
    assert "invalid operation" in captured.out


def test_calculator_help_command(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Calculator()

    captured = capsys.readouterr()
    assert "Available commands" in captured.out


def test_calculator_invalid_sentence(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(["add 2 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Calculator()

    captured = capsys.readouterr()
    assert "invalid operation" in captured.out


def test_calculator_non_numeric_input(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(["add two to five", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Calculator()

    captured = capsys.readouterr()
    assert "invalid operation" in captured.out


def test_calculator_invalid_divide_format(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(["multiply 2 kamelia 7", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Calculator()

    captured = capsys.readouterr()
    assert "invalid operation" in captured.out
