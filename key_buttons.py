"""
created on Sep 07th, 2025

made by FillyRoid
"""

import os
import sys
import subprocess

class Key_buttons:
    def __init__(self, apps):
        self.__applications = apps
        self.__is_error = self.__check_error(self.__applications)


    def __check_error(self, apps):

        for app in apps:
            if not os.path.isfile(app):
                return False

        return True













if __name__ == "__main__":
    apps = {"direct_apps": ["gnome-calculator", ["gnome-screenshot", "--interactive"]],
            "path_apps": []}

    test = Key_buttons()
