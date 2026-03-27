import argparse

from zsh.commands import TerminalCommandExecutor
from zsh.environments import Environments
from zsh.ide import IDE
from zsh.vpn import VpnSetting


def parse_args():
    parser = argparse.ArgumentParser(description="Run Yaana script")

    parser.add_argument("--ide", type=str, default="webstorm", help="Default IDE")
    parser.add_argument("--pr", type=str, default="fe", help="Default project--either 'Backend(be)' or 'Frontend(fe)'")
    args = parser.parse_args()

    default_ide, default_pr = args.ide, args.pr
    return default_ide, default_pr


def main():
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


if __name__ == "__main__":
    main()

