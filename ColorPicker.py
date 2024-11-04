from colorthief import ColorThief
import os
import pandas as pd

cover_list = os.listdir('Cover')

cover_color_list =[]

for cover in cover_list:
    #load Cover
    color_thief = ColorThief('Cover/' + cover)

    # get dominant color
    dominant_color = color_thief.get_color(quality=1)

    #save color
    cover_color_list.append([int(cover[:-4]), dominant_color])

df = pd.DataFrame(cover_color_list,columns=['ID', 'RGB'])

print(df.sort_values(by='ID'))