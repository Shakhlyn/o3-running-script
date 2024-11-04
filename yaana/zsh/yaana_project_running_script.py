import subprocess

class TerminalCommandExecutor:
    def __init__(self, project_path):
        self.project_path = project_path
        self.nvm_source = (
            "export NVM_DIR=\"$HOME/.nvm\"; "
            "[ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\";"
        )
        self.commands = self._generate_commands()

    def _generate_commands(self):
        return [
            f"gnome-terminal --tab -- zsh -c 'cd {self.project_path}; ssh nsdev_mu; exec zsh'",
            f"gnome-terminal --tab -- zsh -c 'cd {self.project_path}; source venv/bin/activate; python manage.py runserver; exec zsh'",
            f"gnome-terminal --tab -- zsh -c 'cd {self.project_path}; {self.nvm_source} nvm use 14.21.3; npm run dev; exec zsh'",
            f"gnome-terminal --tab -- zsh -c 'cd {self.project_path}/frontend; {self.nvm_source} nvm use 14.21.3; npm run dev; exec zsh'",
            f"gnome-terminal --tab -- zsh -c 'cd {self.project_path}; code .'"
        ]

    def execute_commands(self):
        for cmd in self.commands:
            subprocess.run(cmd, shell=True)

