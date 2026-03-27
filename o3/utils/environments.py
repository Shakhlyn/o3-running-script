import os

class Environments(object):

    @staticmethod
    def _get_shell():
            return os.getenv('SHELL')

    @staticmethod
    def _get_project_path():
        """
        since we are running the project after going to the project directory, 'getcwd' is perfect.
        However, for dynamic path, we need to update the logic

        :return: the current directory
        """
        return os.getcwd()

    def get_envs(self):
        try:
            project_path = self._get_project_path()
            shell_name = self._get_shell()

            if shell_name:
                shell = shell_name.split("/")[-1].lower()

                if shell not in ["zsh", "bash"]:
                     raise ValueError(f"Unsupported shell: '{shell}'. Only 'zsh' and 'bash' are supported."
                                      f"Since you are using other than these two, FYKI, muri khan\U0001F61C ")
            else:
                raise EnvironmentError("Could not determine the current shell from the environment.")

            return [shell, project_path]

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
