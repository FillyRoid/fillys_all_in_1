"""
created on Aug 05th, 2025

made by FillyRoid
"""
import os

"""
Frame List:
0. volume mixer
1. apps hotkeys
"""


import json
import gui_applications as ga
import os

def get_apps_data():
    with open("data/apps_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

def get_key_data():
    if os.path.exists("data/keys_apps.json"):
        with open("data/keys_apps.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    return 0



def run():
    apps_data = get_apps_data()
    key_apps = get_key_data()
    full_mode = False       #full mode
    win_title = "Fillys All-in-1"

    #create window
    gui = ga.GUI_general(win_title, apps_data, key_apps, full_mode)

    #get frames
    root = gui.get_root()


    root.mainloop()





#Start programm
if __name__ == "__main__":
    run()