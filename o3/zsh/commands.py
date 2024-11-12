import subprocess

class TerminalCommandExecutor:
    def __init__(self, project_path, shell, ide):
        self.project_path = project_path
        self.shell = shell
        self.ide = ide
        self.nvm_source = (
            "export NVM_DIR=\"$HOME/.nvm\"; "
            "[ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\";"
        )
        self.commands = self._generate_commands()

    def _generate_commands(self):
        return [
            f"gnome-terminal --tab -- {self.shell} -c 'cd {self.project_path}; ssh nsdev_mu; exec {self.shell}'",
            f"gnome-terminal --tab -- {self.shell} -c 'cd {self.project_path}; source venv/bin/activate; \
                   if [ -z \"$VIRTUAL_ENV\" ]; then echo \"Failed to activate venv\"; else echo \"venv activated\"; fi; \
                   python manage.py runserver; exec {self.shell}'",
            f"gnome-terminal --tab -- {self.shell} -c 'cd {self.project_path}; {self.nvm_source} nvm use 14.21.3 && npm run dev; exec {self.shell}'",
            f"gnome-terminal --tab -- {self.shell} -c 'cd {self.project_path}/frontend; {self.nvm_source} nvm use 14.21.3 && npm run dev; exec {self.shell}'",
            f"gnome-terminal --tab -- {self.shell} -c 'cd {self.project_path}; {self.ide}'"
        ]

    def execute_commands(self):
        for cmd in self.commands:
            try:
                subprocess.run(cmd, shell=True)
            except Exception as e:
                print(f"Error executing command: {cmd}\n{e}")
