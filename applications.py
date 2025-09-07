"""
created on Aug 05th, 2025

made by FillyRoid
"""

import subprocess
import re


class Sound_settings:
    def __init__(self):
        self.__is_error = self.__error_check()

    #check, if the sound mixer has an error
    def __error_check(self):
        try:
            subprocess.run(["amixer", "--version"], capture_output=True, check=True)
            return True
        except:
            print("Error by Loading Sound Controller!")
            return False


    #getter: current volumen
    def get_current_volume(self):
        result = subprocess.run(
            ['amixer', 'get', 'Master'],
            capture_output=True, text=True, check=True
        )

        # Suche nach Lautstärke in Prozent
        match = re.search(r'\[(\d+)%\]', result.stdout)
        if match:
            match = match.group(1)
            print(f"Volume: {match}")
            return int(match)
        return None

    #setter: volume
    def set_volume(self, volume):
        if 0 <= volume <= 100:
            subprocess.run(['amixer', 'set', 'Master', f'{volume}%'],capture_output=True, check=True)
            print(f"Volume set: {volume}%")

    #getter: mute
    def get_mute(self):
        check = subprocess.run(["amixer", "get", "Master"], capture_output=True, text=True, check=True)

        if "[off]" in check.stdout:
            print("Volume muted")
            return True
        else:
            print("Volume active")
            return False

    #setter: mute
    def set_mute(self):
        subprocess.run(['amixer', 'set', 'Master', 'toggle'],capture_output=True, check=True)

        self.get_mute()












if __name__ == "__main__":
    """test = Sound_settings()
    print(test.is_error())
    test.get_current_volume()
    test.set_volume(20)
    test.get_mute()
    test.set_mute()"""

    pass
