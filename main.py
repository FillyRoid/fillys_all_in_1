"""
created on Aug 05th, 2025

made by FillyRoid
"""




"""
Frame List:
0. volume mixer
1. apps hotkeys
"""


import json
import gui_applications as ga

def get_data():
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def run():
    data = get_data()
    full_mode = False       #full mode
    win_title = "Fillys All-in-1"

    #create window
    gui = ga.GUI_general(win_title, data, full_mode)

    #get frames
    root = gui.get_root()


    root.mainloop()





#Start programm
if __name__ == "__main__":
    run()