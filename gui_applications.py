"""
created on Aug 24th, 2025

made by FillyRoid
"""

import customtkinter as ctk
import volume_mixer as volm
import data_config

#general Elements
class GUI_general:
    def __init__(self, win_title, data, full_mode):
        self.__full_mode = full_mode
        self.__frame_data = data

        self.__win_width, self.__win_height = data_config.get_size(self.__frame_data, self.__full_mode)


        self.__root = ctk.CTk()     #declarate root
        self.__root.geometry(f"{self.__win_width}x{self.__win_height}")
        self.__root.title(win_title)
        self.__root.attributes("-topmost", 1)
        self.__root.resizable(False, False)

        # main frame for apps
        self.__main_frame = ctk.CTkFrame(self.__root, fg_color="#B0BDD9")
        self.__main_frame.place(x=20, y=20)

        #get main button
        self.__get_btn()

        self.__declare_all_apps()
        self.__set_mode()


    #getter: root
    def get_root(self):
        return self.__root



    #widgets
    #Button
    def __get_btn(self):
        self.__active_button = ctk.CTkButton(self.__root, width=20, height=20, text="", command=self.__set_mode, hover=False, border_color="#645A73", border_width=2)
        self.__active_button.place(x=0, y=0)


    def __declare_all_apps(self):
        for i in range(len(self.__frame_data["name"])):
            self.__frame_data["gui_frame"].append(GUI_sound_settings(self.__main_frame))



    #setter: widgets
    def __set_mode(self):
        if self.__full_mode:
            self.__win_width, self.__win_height = data_config.get_size(self.__frame_data, self.__full_mode)
            self.__root.geometry(f"{self.__win_width}x{self.__win_height}")

            # clear the hole root:
            for widget in self.__main_frame.winfo_children():
                widget.destroy()

            for i in range(len(self.__frame_data["gui_frame"])):
                self.__frame_data["gui_frame"][i].get_app(
                    self.__frame_data["open_size"][i][0],
                    self.__frame_data["open_size"][i][1],
                    0,
                    0,
                    self.__full_mode)

            self.__active_button.configure(fg_color="#AD3434")
            self.__full_mode = False


        else:
            self.__win_width, self.__win_height = data_config.get_size(self.__frame_data, self.__full_mode)
            self.__root.geometry(f"{self.__win_width}x{self.__win_height}")

            # clear the hole root:
            for widget in self.__main_frame.winfo_children():
                widget.destroy()

            for i in range(len(self.__frame_data["gui_frame"])):
                self.__frame_data["gui_frame"][i].get_app(
                    self.__frame_data["closed_size"][i][0],
                    self.__frame_data["closed_size"][i][1],
                    0,
                    0,
                    self.__full_mode)

            self.__active_button.configure(fg_color="#347F3A")
            self.__full_mode = True










#Volume Mixer
class GUI_sound_settings:
    def __init__(self, main_frame):
        self.__sound_app = volm.Sound_settings()
        self.__main_frame = main_frame
        self.__full_mode = False




    def get_app(self, app_width, app_height, row, column, full_mode):
        if full_mode:
            # main frame
            self.__app_frame = ctk.CTkFrame(self.__main_frame, width=app_width, height=app_height, fg_color="#B0BDD9")
            self.__app_frame.grid(row=row, column=column)

            # label (volume output)
            self.__label = ctk.CTkLabel(self.__app_frame, text=self.__get_volume())
            self.__label.place(x=20, y=14)


            # slider
            self.__slider = ctk.CTkSlider(self.__app_frame, from_=0, to=100, number_of_steps=100, command=self.__set_volume)
            self.__slider.set(self.__get_volume())
            self.__slider.place(x=50, y=20)

            # switch (mute)
            self.__check_var = ctk.BooleanVar(value=self.__sound_app.get_mute())
            self.__switch = ctk.CTkSwitch(self.__app_frame, switch_width=25, switch_height=15, text="",
                                          variable=self.__check_var, onvalue=True, offvalue=False,
                                          command=self.__mute_volume)
            self.__switch.place(x=260, y=17)

            self.__full_mode = full_mode
            self.__get_mute_update()

        else:
            # main frame
            self.__app_frame = ctk.CTkFrame(self.__main_frame, width=app_width, height=app_height, fg_color="#B0BDD9")
            self.__app_frame.grid(row=row, column=column)

            # switch (mute)
            self.__check_var = ctk.BooleanVar(value=self.__sound_app.get_mute())
            self.__switch = ctk.CTkSwitch(self.__app_frame, switch_width=25, switch_height=15, text="",
                                          variable=self.__check_var, onvalue=True, offvalue=False,
                                          command=self.__mute_volume)
            self.__switch.place(x=50, y=12)

            # label (volume output)
            self.__label = ctk.CTkLabel(self.__app_frame, text=self.__get_volume())
            self.__label.place(x=15, y=10)

            # reduce button
            self.__reduce_btn = ctk.CTkButton(self.__app_frame, text="-5", width=27, height=15, fg_color="#950F0F", command=lambda: self.__set_volume(0, add=False))
            self.__reduce_btn.place(x=15, y=40)

            # add button
            self.__add_btn = ctk.CTkButton(self.__app_frame, text="+5", width=25, height=15, fg_color="#225326", command=lambda: self.__set_volume(0, add=True))
            self.__add_btn.place(x=45, y=40)

            self.__full_mode = full_mode
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
            if self.__full_mode:
                self.__slider.configure(fg_color="#CACACC",
                                        progress_color="#E1E1E3",
                                        button_color="#4B66A3",
                                        border_color="#59595C")
            else:
                self.__add_btn.configure(fg_color="#9E9E9E")
                self.__reduce_btn.configure(fg_color="#9E9E9E")

        else:
            if self.__full_mode:
                self.__slider.configure(fg_color="#8CA7DE",
                                        progress_color="white",
                                        button_color="#4B66A3",
                                        border_color="#0F1112")
            else:
                self.__add_btn.configure(fg_color="#225326")
                self.__reduce_btn.configure(fg_color="#950F0F")


    #getter: volume
    def __get_volume(self):
        return self.__sound_app.get_current_volume()


    #setter: volume
    def __set_volume(self, value, add=True):
        curr_vol = self.__sound_app.get_current_volume()

        if self.__full_mode:
            #set new valume on pc
            self.__sound_app.set_volume(value)
            #update the volume label in GUI
            self.__label.configure(text=curr_vol)
        else:
            if add:
                if curr_vol + 5 > 100:
                    curr_vol = 100
                else:
                    curr_vol += 5
            else:
                if curr_vol - 5 < 0:
                    curr_vol = 0
                else:
                    curr_vol -= 5

            self.__sound_app.set_volume(curr_vol)
            self.__label.configure(text=curr_vol)


    #set: bar color switch by mute
    def __mute_volume(self):
        if self.__check_var.get():
            self.__sound_app.set_mute()

            if self.__full_mode:
                self.__slider.configure(fg_color="#CACACC",
                                        progress_color="#E1E1E3",
                                        button_color="#4B66A3",
                                        border_color="#59595C")
            else:
                self.__add_btn.configure(fg_color="#9E9E9E")
                self.__reduce_btn.configure(fg_color="#9E9E9E")

        else:
            self.__sound_app.set_mute()

            if self.__full_mode:
                self.__slider.configure(fg_color="#8CA7DE",
                                        progress_color="white",
                                        button_color="#4B66A3",
                                        border_color="#0F1112")
            else:
                self.__add_btn.configure(fg_color="#225326")
                self.__reduce_btn.configure(fg_color="#950F0F")

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("700x700")

    test = GUI_sound_settings(root, 330, 50)



    root.mainloop()