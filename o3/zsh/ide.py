import os.path
import subprocess
from importlib import resources


class IDE:
    def __init__(self):
        self.config_file = self._get_config_file_path()
        self.ides = {
            "1": 'webstorm .',
            "2": 'code .',
            "3": f'{self._get_pycharm_path()} .',
        }
        self.ide_codes = ['1', '2', '3']


    @staticmethod
    def _get_config_file_path():
        with resources.path(__package__, "config.txt") as config_path:
            return str(config_path)


    @staticmethod
    def _take_input_for_ide_code():
        return input("""
        Please select the IDE you want to use for coding:
            Type 1, 2, or 3 and press Enter.
            
            1: WebStorm
            2: VS Code
            3: PyCharm            
            """)


    def _get_pycharm_path(self):
        """
        check if the file is present in the package. If present, check if the ide path is present.
        If the path is present, read return the path
        Otherwise, create a file and write path in that file after finding the path
        """
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as file:
                pycharm_path = file.read().strip()
                if pycharm_path:
                    print(f"\U0001F603 Found pycharm: {pycharm_path}")
                    return pycharm_path

        # find the path of pycharm
        print("\U0001F914 Ha! Path is not saved!\n"
              "\t\t\U0001F50E We are trying to locate the pycharm bin file\n"
              "\t\t Please wait for a moment ...\n"
              "\n\U0001F4DD Writing the path")

        result = subprocess.run(["find", "/", "-name", "pycharm.sh"], capture_output=True, text=True)
        pycharm_path = result.stdout.strip().splitlines()[0] if result.stdout else None

        if pycharm_path:
            with open(self.config_file, 'w') as file:
                file.write(pycharm_path)
                print("\U0001F44F Hurrah! The path has been saved!")
            return pycharm_path
        else:
            raise FileNotFoundError("PyCharm not found. Please check the installation path.")


    def _get_ide_code(self):
        ide_code = self._take_input_for_ide_code()

        while ide_code not in self.ide_codes:
            print(""""
            \n\t \U0001F914 I assume you don't like these ides!"
            \U0001F614 Unfortunately, currently we only support these three ides.      
                  \n\U0001F449 Please select 1 or 2 or 3.
                  If you like to use other ides, please let me know. I'll  be happy \U0001F603 to extend""")
            ide_code = self._take_input_for_ide_code()

        return ide_code


    def get_ide(self):
        try:
            ide_code = self._get_ide_code()
            if ide_code:
                return self.ides[ide_code]
            else:
                return "No ide found!"
        except:
            raise ValueError("No IDE code found. Please contact me.")
