import colorgram
colors = colorgram.extract('hurst-spot-painting.jpg', 12)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    rgb_colors.append(tup)

rgb_colors = [(230, 227, 223), (164, 153, 138), (238, 232, 234), (229, 236, 232), (226, 232, 238), (148, 91, 59), (56, 33, 20), (173, 148, 53), (42, 103, 153), (31, 40, 57), (127, 170, 191), (221, 207, 121)]

