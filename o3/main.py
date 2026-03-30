from utils.commands import TerminalCommandExecutor
from utils.environments import Environments
from utils.ide import IDE
from utils.vpn import VpnSetting
from utils.arguments import Arguments


def main():
    try:
        arguments = Arguments()
        [preferred_ide, preferred_pr] = arguments.parse_args()

        ide = IDE(preferred_ide)
        settings = Environments()
        vpn_settings = VpnSetting()

        # configure the vpn first
        # vpn_settings.run_vpn()


        ide = ide.get_ide()
        print(ide)
        [shell, project_path] = settings.get_envs()

        print(f"Working shell: {shell}\n"
              f"Project path: {project_path}\n")

        executor = TerminalCommandExecutor(project_path, shell, ide)
        # executor.execute_commands()

        print(f"*** Live Long and Prosper *** \U0001F596\n")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

