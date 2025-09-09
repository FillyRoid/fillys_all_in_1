"""
created on Sep 08th, 2025

made by FillyRoid
"""



def get_size(data, is_active):


    win_width = 0

    apps_amount = len(data["name"]) - 1
    max_height = 0

    if is_active:
        for app in data["open_size"]:
            win_width += app[0]
            if max_height < app[1]:
                max_height = app[1]

    else:
        for app in data["closed_size"]:
            win_width += app[0]
            if max_height < app[1]:
                max_height = app[1]


    win_width += 40 + (10*apps_amount)
    max_height += 40


    return win_width, max_height


