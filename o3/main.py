import os

from zsh.commands import TerminalCommandExecutor
from zsh.settings import Environments
from zsh.ide import IDE

if __name__ == "__main__":

    try:
        ide = IDE()
        settings = Environments()

        ide = ide.get_ide()
        [shell, project_path] = settings.get_envs()

        print(f"Working shell: {shell}\n"
              f"Project path: {project_path}\n")

        executor = TerminalCommandExecutor(project_path, shell, ide)
        executor.execute_commands()

        print(f"*** Live Long and Prosper *** \U0001F596\n")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
