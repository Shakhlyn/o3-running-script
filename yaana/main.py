from zsh.yaana_project_running_script import TerminalCommandExecutor


if __name__ == "__main__":
    project_path = "~/project/office/yaana/o3"
    executor = TerminalCommandExecutor(project_path)
    executor.execute_commands()
