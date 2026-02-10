



def it_command_simulator(command : str) -> str :

    #git_add = "git add <filename>"
    #description_add = "Stage all changes or specific file filename for the next commit."

    #git_cached = "git rm --cached <filename>"
    #description_cached = "Unstage file <filename> while retaining the changes in the working directory."

    #git_commit = "git commit -m <commit message>"
    #description_commit = "Commit changes to the repository with a descriptive message <commit message>."

    #git_push = "git push"
    #description_push = "Upload your commits to the remote repository."

    #git_stash = "git stash" 
    #description_stash = "Temporarily shelves changes in your working directory so you can work on a different task."

    #git_stash_push = "git stash push -m <stash message>"
    #description_stash_push = "Stashes changes with a custom message <stash message> for easy identification."

    #git_stash_apply = "git stash apply"
    #description_stash_apply = "Applies the most recently stashed changes."

    #git_stash_apply_name = "git stash apply <stash-name>"
    #description_stash_apply_name = "Applies the stashed changes with the specified name <stash-name>."

    if command.startswith("git add"):
        git_message = command.split('git add')[1]
        print(f'"Stage all changes or specific file {git_message} for the next commit.')
        return 
    
    if command.startswith("git rm --cached"):
        git_message = command.split('git rm --cached')[1]
        print(f'Unstage file {git_message} while retaining the changes in the working directory.')
        return 
    
    if command.startswith("git commit -m"):
        git_message = command.split('git commit -m')[1]
        print(f'Commit changes to the repository with a descriptive message {git_message}.')
        return 
    
    if command.startswith("git push"):
        print(f'Upload your commits to the remote repository.')
        return 
    
    if command.startswith("git stash"):
        print(f'Temporarily shelves changes in your working directory so you can work on a different task.')
        return 
    
    if command.startswith("git stash push -m"):
        git_message = command.split('git stash push -m')[1]
        print(f'Stashes changes with a custom message {git_message} for easy identification.')
        return 
    
    if command.startswith("git stash apply"):
        print(f'Applies the most recently stashed changes.')
        return 
    
    if command.startswith("git stash apply "):
        git_message = command.split('git stash push -m')[1]
        print(f'Applies the stashed changes with the specified name {git_message}.')
        return 
    

    return 






enter_command = 'git stash push -m kamelia'
print(it_command_simulator(enter_command))

## output - 'Unstage file readme.md while retaining the changes in the working directory.'


#Command,Description
"git add <filename>","Stage all changes or specific file <filename> for the next commit."
"git rm --cached <filename>","Unstage file <filename> while retaining the changes in the working directory."
"git commit -m <commit message>","Commit changes to the repository with a descriptive message <commit message>."
"git push","Upload your commits to the remote repository."
"git stash","Temporarily shelves changes in your working directory so you can work on a different task."
"git stash push -m <stash message>","Stashes changes with a custom message <stash message> for easy identification."
"git stash apply","Applies the most recently stashed changes."
"git stash apply <stash-name>","Applies the stashed changes with the specified name <stash-name>."
