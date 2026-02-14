import pytest
from solution.exercise3 import git_command_simulator, INVALID_COMMAND


@pytest.mark.parametrize(
    "input,expected_output",
    [
        (
            "git add readme.md",
            "Stage all changes or specific file readme.md for the next commit.",
        ),
        (
            "git rm --cached readme.md",
            "Unstage file readme.md while retaining the changes in the working directory.",
        ),
        (
            'git commit -m "initial commit"',
            'Commit changes to the repository with a descriptive message "initial commit".',
        ),
        ("git push", "Upload your commits to the remote repository."),
        (
            "git stash",
            "Temporarily shelves changes in your working directory so you can work on a different task.",
        ),
        (
            'git stash push -m "finished exercise"',
            'Stashes changes with a custom message "finished exercise" for easy identification.',
        ),
        ("git stash apply", "Applies the most recently stashed changes."),
        (
            "git stash apply my_stash",
            "Applies the stashed changes with the specified name my_stash.",
        ),
        ("unknown command", INVALID_COMMAND),
        ("git add", INVALID_COMMAND),
        ("git commit -m", INVALID_COMMAND),
    ],
)
def test_git_command_simulator(input: str, expected_output: str) -> None:
    assert git_command_simulator(input) == expected_output
