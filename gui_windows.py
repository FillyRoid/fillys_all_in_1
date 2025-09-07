"""
created on Aug 24th, 2025

made by FillyRoid
"""
from decimal import Clamped

import customtkinter as ctk
import applications as apps


class GUI_sound_settings:
    def __init__(self, root, win_width, win_height):
        self.__sound_app = apps.Sound_settings()
        self.__curr_volume = self.__sound_app.get_current_volume()

        #main frame
        self.__main_frame = ctk.CTkFrame(root, width=win_width, height=win_height, fg_color="#B0BDD9")
        self.__main_frame.grid_propagate(0)
        self.__main_frame.grid(row=0, column=0, padx=20, pady=20)

        #slider
        self.__slider = ctk.CTkSlider(self.__main_frame,
                                      from_=0,
                                      to=100,
                                      number_of_steps=100,
                                      command=self.__set_volume)
        self.__slider.set(self.__curr_volume)
        self.__slider.grid(row=0, column=0, padx=30, pady=20)

        #volume output
        self.__label = ctk.CTkLabel(self.__main_frame, text=self.__curr_volume)
        self.__label.grid(row=0, column=1)

        #mute_button
        self.__check_var = ctk.BooleanVar(value=self.__sound_app.get_mute())
        self.__switch = ctk.CTkSwitch(self.__main_frame, switch_width=25, switch_height=15, text="", variable=self.__check_var, onvalue=True, offvalue=False, command=self.__mute_volume)
        self.__switch.grid(row=0, column=2, padx=20)

        self.__get_mute_update()

    """
    def check_for_updates(self, root):
        new_volume = self.__sound_app.get_current_volume()
        is_muted = self.__sound_app.get_mute()

        if not self.__curr_volume == new_volume and not self.__check_var == is_muted:
            self.__curr_volume = new_volume
            self.__check_var = ctk.BooleanVar(value=is_muted)

            self.__slider.set(self.__curr_volume)
            self.__label.configure(text=self.__curr_volume)
            self.__switch.configure(variable=is_muted)
    """


    #check: if muted
    def __get_mute_update(self):
        if self.__check_var.get():
            self.__slider.configure(fg_color="#CACACC",
                                    progress_color="#E1E1E3",
                                    button_color="#4B66A3",
                                    border_color="#59595C")

        else:
            self.__slider.configure(fg_color="#8CA7DE",
                                    progress_color="white",
                                    button_color="#4B66A3",
                                    border_color="#0F1112")


    #setter: volume
    def __set_volume(self, value):
        #set new valume on pc
        self.__sound_app.set_volume(value)
        #update the volume label in GUI
        self.__label.configure(text=self.__sound_app.get_current_volume())


    #set: bar color switch by mute
    def __mute_volume(self):
        if self.__check_var.get():
            self.__sound_app.set_mute()
            self.__slider.configure()
            self.__slider.configure(fg_color="#CACACC",
                                    progress_color="#E1E1E3",
                                    button_color="#4B66A3",
                                    border_color="#59595C")

        else:
            self.__sound_app.set_mute()
            self.__slider.configure()
            self.__slider.configure(fg_color="#8CA7DE",
                                    progress_color="white",
                                    button_color="#4B66A3",
                                    border_color="#0F1112")

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("700x700")

    test = GUI_sound_settings(root, 330, 50)



    root.mainloop()