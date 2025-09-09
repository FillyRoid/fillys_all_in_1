"""
created on Sep 07th, 2025

made by FillyRoid
"""


import subprocess

class Key_buttons:
    def __init__(self, apps):
        self.__applications = apps
        self.__is_error = self.__error_check()

    def __error_check(self):
        err_list = []

        for app in self.__applications:
            try:
                if type(app) == list:
                    subprocess.run(app + ["--version"])
            except:
                err_list.append(f"Error by Loading {app}!")

        return err_list

    def get_error_list(self):
        return self.__is_error


    def open_file(self, app):
        subprocess.Popen(app)














if __name__ == "__main__":
    apps = ["gnome-calculator", ["gnome-screenshot", "--interactive"], ]

    test = Key_buttons(apps)

