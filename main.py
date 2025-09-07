"""
created on Aug 05th, 2025

made by FillyRoid
"""


import customtkinter as ctk
import gui_windows as gw


def get_size():
    apps_sizes = {"sound": [330, 50]}

    win_width = 0
    win_height = 0


    for app in apps_sizes.values():
        win_width += app[0]
        win_height += app[1]

    win_width += 40
    win_height += 40

    return win_width, win_height







def run():
    win_width, win_height = get_size()
    win_title = "Fillys All-in-1"

    root = ctk.CTk()
    root.geometry(f"{win_width}x{win_height}")
    root.title(win_title)
    root.attributes("-topmost", 1)

    sound_apps = gw.GUI_sound_settings(root, 330, 50)

    root.mainloop()







#Start programm
if __name__ == "__main__":
    run()