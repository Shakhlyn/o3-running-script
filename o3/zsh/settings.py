import os

class Environments(object):

    def _get_shell(self):
            return os.getenv('SHELL')

    def _get_project_path(self):
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
