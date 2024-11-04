import os

from zsh.yaana_project_running_script import TerminalCommandExecutor


if __name__ == "__main__":
    try:
        project_path = os.getcwd()
        current_shell = os.environ.get('SHELL')

        print("Path for the prject: ", project_path)

        if current_shell:
            formatted_shell_name = current_shell.split("/")[-1].lower()

            if formatted_shell_name not in ["zsh", "bash"]:
                raise ValueError(f"Unsupported shell: '{formatted_shell_name}'. Only 'zsh' and 'bash' are supported."
                                 f"Since you are using other than these two, FYKI, muri khan\U0001F61C ")

            print(f"Current shell: {formatted_shell_name}")

        else:
            raise EnvironmentError("Could not determine the current shell from the environment.")

        executor = TerminalCommandExecutor(project_path, formatted_shell_name)
        executor.execute_commands()

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
