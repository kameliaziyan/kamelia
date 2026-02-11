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


def it_command_simulator(command: str) -> str:

    len_command = len(command.split())
    # print(len_command)

    if command.startswith(GIT_ADD):
        git_message = command.split("git add")[1]
        print(f'"Stage all changes or specific file {git_message} for the next commit.')
        return f'"Stage all changes or specific file {git_message} for the next commit.'

    if command.startswith(GIT_CACHED):
        git_message = command.split("git rm --cached")[1]
        print(
            f"Unstage file {git_message} while retaining the changes in the working directory."
        )
        return f"Unstage file {git_message} while retaining the changes in the working directory."

    if command.startswith(GIT_COMMIT):
        git_message = command.split("git commit -m")[1]
        print(
            f"Commit changes to the repository with a descriptive message {git_message}."
        )
        return f"Commit changes to the repository with a descriptive message {git_message}."

    if command.startswith(GIT_PUSH):
        print("Upload your commits to the remote repository.")
        return "Upload your commits to the remote repository."

    if command.startswith(GIT_STASH) and len_command == 2:
        print(
            "Temporarily shelves changes in your working directory so you can work on a different task."
        )
        return "Temporarily shelves changes in your working directory so you can work on a different task."

    if command.startswith(GIT_STASH_PUSH) and len_command >= 5:
        git_message = command.split("git stash push -m")[1]
        print(
            f"Stashes changes with a custom message {git_message} for easy identification."
        )
        return f"Stashes changes with a custom message {git_message} for easy identification."

    if command.startswith(GIT_STASH_APPLY) and len_command == 3:
        print("Applies the most recently stashed changes.")
        return "Applies the most recently stashed changes."

    if command.startswith(GIT_STASH_APPLY_NAME) and len_command == 4:
        git_message = command.split("git stash apply")[1]
        print(f"Applies the stashed changes with the specified name {git_message}.")
        return f"Applies the stashed changes with the specified name {git_message}."

    return "Error: Unsupported or invalid git command."


enter_command = 'git commit -m "all done"'
print(it_command_simulator(enter_command))


# git_add = "git add <filename>"
# description_add = "Stage all changes or specific file filename for the next commit."

# git_cached = "git rm --cached <filename>"
# description_cached = "Unstage file <filename> while retaining the changes in the working directory."

# git_commit = "git commit -m <commit message>"
# description_commit = "Commit changes to the repository with a descriptive message <commit message>."

# git_push = "git push"
# description_push = "Upload your commits to the remote repository."

# git_stash = "git stash"
# description_stash = "Temporarily shelves changes in your working directory so you can work on a different task."

# git_stash_push = "git stash push -m <stash message>"
# description_stash_push = "Stashes changes with a custom message <stash message> for easy identification."

# git_stash_apply = "git stash apply"
# description_stash_apply = "Applies the most recently stashed changes."

# git_stash_apply_name = "git stash apply <stash-name>"
# description_stash_apply_name = "Applies the stashed changes with the specified name <stash-name>."
