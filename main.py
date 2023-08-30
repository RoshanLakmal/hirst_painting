# This is a sample Python script.
import colorgram

number_of_colors = 6
colors = colorgram.extract('painting.jpg', number_of_colors)

color_list = []

def generate_color_tuple(rgb_obj):
    genereated_tuple = (rgb_obj.r,rgb_obj.g,rgb_obj.b)
    return genereated_tuple

for color_item in colors:
    rgb_obj = color_item.rgb
    tuple_color =generate_color_tuple(rgb_obj)
    color_list.append(tuple_color)

print(color_list)