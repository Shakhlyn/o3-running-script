import sys

from zsh.commands import TerminalCommandExecutor
from zsh.environments import Environments
from zsh.ide import IDE
from zsh.vpn import VpnSetting

if __name__ == "__main__":

    try:
        ide = IDE()
        settings = Environments()
        vpn_settings = VpnSetting()

        # configure the vpn first
        vpn_settings.run_vpn()

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
