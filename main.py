import colorgram
import os

# Ensure the working directory is the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

colors =colorgram.extract("image.jpg", 30)
color_list =[]

for col in colors:
    r =col.rgb.r
    g =col.rgb.g
    b =col.rgb.b

    new_col =(r,g,b)
    color_list.append(new_col)
print(color_list)    