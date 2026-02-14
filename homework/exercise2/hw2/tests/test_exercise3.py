from solution.exercise3 import git_command_simulator


def test_git_add() -> None:
    command = "git add readme.md"
    result = git_command_simulator(command)
    right_answer = "Stage all changes or specific file readme.md for the next commit."
    assert result == right_answer


def test_git_rm_cached() -> None:
    command = "git rm --cached readme.md"
    result = git_command_simulator(command)
    right_answer = (
        "Unstage file readme.md while retaining the changes in the working directory."
    )
    assert result == right_answer


def test_git_commit() -> None:
    command = 'git commit -m "initial commit"'
    result = git_command_simulator(command)
    right_answer = (
        'Commit changes to the repository with a descriptive message "initial commit".'
    )
    assert result == right_answer


def test_git_push() -> None:
    command = "git push"
    result = git_command_simulator(command)
    right_answer = "Upload your commits to the remote repository."
    assert result == right_answer


def test_git_stash() -> None:
    command = "git stash"
    result = git_command_simulator(command)
    right_answer = "Temporarily shelves changes in your working directory so you can work on a different task."
    assert result == right_answer


def test_git_stash_push() -> None:
    command = 'git stash push -m "finished exercise"'
    result = git_command_simulator(command)
    right_answer = 'Stashes changes with a custom message "finished exercise" for easy identification.'
    assert result == right_answer


def test_git_stash_apply() -> None:
    command = "git stash apply"
    result = git_command_simulator(command)
    assert result == "Applies the most recently stashed changes."


def test_invalid_command() -> None:
    command = "unknown command"
    result = git_command_simulator(command)
    assert result == "Invalid Command"
