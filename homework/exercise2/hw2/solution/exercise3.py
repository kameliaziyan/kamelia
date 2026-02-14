GIT_ADD = "git add"
DESCRIPTION_ADD = "Stage all changes or specific file filename for the next commit."

GIT_CACHED = "git rm --cached"
DESCRIPTION_CACHED = (
    "Unstage file <filename> while retaining the changes in the working directory."
)

GIT_COMMIT = "git commit -m"
DESCRIPTION_COMMIT = (
    "Commit changes to the repository with a descriptive message <commit message>."
)

GIT_PUSH = "git push"
DESCRIPTION_PUSH = "Upload your commits to the remote repository."

GIT_STASH = "git stash"
DESCRIPTION_STASH = "Temporarily shelves changes in your working directory so you can work on a different task."

GIT_STASH_PUSH = "git stash push -m"
DESCRIPTION_STASH_PUSH = (
    "Stashes changes with a custom message <stash message> for easy identification."
)

GIT_STASH_APPLY = "git stash apply"
DESCRIPTION_STASH_APPLY = "Applies the most recently stashed changes."

GIT_STASH_APPLY_NAME = "git stash apply"
DESCRIPTION_STASH_APPLY_NAME = (
    "Applies the stashed changes with the specified name <stash-name>."
)

INVALID_COMMAND = "Invalid Command"


def handle_basic_commands(command: str) -> str | None:
    match command:
        case cmd if cmd.startswith(f"{GIT_ADD} "):
            filename = cmd.replace(GIT_ADD, "").strip()
            return DESCRIPTION_ADD.replace("filename", filename)

        case cmd if cmd.startswith(f"{GIT_CACHED} "):
            filename = cmd.replace(GIT_CACHED, "").strip()
            return DESCRIPTION_CACHED.replace("<filename>", filename)

        case cmd if cmd.startswith(f"{GIT_COMMIT} "):
            message = cmd.replace(GIT_COMMIT, "").strip()
            return DESCRIPTION_COMMIT.replace("<commit message>", message)

        case cmd if cmd == GIT_PUSH:
            return DESCRIPTION_PUSH

    return None


def handle_stash_commands(command: str) -> str | None:
    match command:
        case cmd if cmd == GIT_STASH:
            return DESCRIPTION_STASH

        case cmd if cmd.startswith(f"{GIT_STASH_PUSH} "):
            message = cmd.replace(GIT_STASH_PUSH, "").strip()
            return DESCRIPTION_STASH_PUSH.replace("<stash message>", message)

        case cmd if cmd == GIT_STASH_APPLY:
            return DESCRIPTION_STASH_APPLY

        case cmd if cmd.startswith(f"{GIT_STASH_APPLY_NAME} "):
            stash_name = cmd.replace(GIT_STASH_APPLY_NAME, "").strip()
            return DESCRIPTION_STASH_APPLY_NAME.replace(
                "<stash-name>", stash_name
            )

    return None


def git_command_simulator(command: str) -> str:
    result = handle_basic_commands(command)
    if result is not None:
        return result

    result = handle_stash_commands(command)
    if result is not None:
        return result

    return INVALID_COMMAND
