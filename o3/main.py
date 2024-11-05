import os

from zsh.commands import TerminalCommandExecutor
from zsh.settings import Environments

if __name__ == "__main__":
    settings = Environments()
    try:
        [shell, project_path] = settings.get_envs()
        print(f"Working shell: {shell}\n"
              f"Project path: {project_path}")

        executor = TerminalCommandExecutor(project_path, shell)
        executor.execute_commands()

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
