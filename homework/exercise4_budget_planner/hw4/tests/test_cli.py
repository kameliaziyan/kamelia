from solution.cli import CLI
from pytest import CaptureFixture


def test_exit_action() -> None:
    cli = CLI()
    result = cli._process_action("7")

    assert result is False


def test_invalid_option(capsys: CaptureFixture[str]) -> None:
    cli = CLI()

    result = cli._process_action("99")

    captured = capsys.readouterr()

    assert result is True
    assert "Invalid option" in captured.out


def test_clear_all_action(capsys: CaptureFixture[str]) -> None:
    cli = CLI()
    cli.budget.add("Salary", 5000, "income")

    cli._process_action("6")

    assert len(cli.budget.incomes) == 0
