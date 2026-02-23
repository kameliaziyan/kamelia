import responses
from solution.budget_planner_ui import UI

BASE_URL = "http://localhost:8000"


@responses.activate
def test_safe_getpass():
    responses.add(
        responses.GET,
        f"{BASE_URL}/summary",
        json={"data": {"remaining_budget": 4000}},
        status=200,
    )

    ui = UI()
    result = ui._safe_get("/summary")

    assert result == {"data": {"remaining_budget": 4000}}


@responses.activate
def test_clear_allpass(capsys):
        responses.add(
            responses.DELETE,
            f"{BASE_URL}/clear",
            status=200,
        )

        ui = UI()
        ui._clear_all_action()

        captured = capsys.readouterr()
        assert "All data cleared successfully!" in captured.out


@responses.activate
def test_add_incomepass(monkeypatch, capsys):
        responses.add(
            responses.POST,
            f"{BASE_URL}/income",
            status=200,
        )

        inputs = iter(["Salary", "5000"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        ui = UI()
        ui._add_income_action()

        captured = capsys.readouterr()
        assert "Income added successfully!" in captured.out