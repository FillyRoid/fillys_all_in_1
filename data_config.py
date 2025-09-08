"""
created on Sep 08th, 2025

made by FillyRoid
"""



def get_size(data, is_active):


    win_width = 0
    win_height = 0

    if is_active:
        for app in data["open_size"]:
            win_width += app[0]
            win_height += app[1]

            print(app)
    else:
        for app in data["closed_size"]:
            win_width += app[0]
            win_height += app[1]

            print(app)

    win_width += 40
    win_height += 40

    print([win_width, win_height])

    return win_width, win_height


