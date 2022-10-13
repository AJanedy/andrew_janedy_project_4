import arcade

project_file= open("nationsPop.txt", 'r')
file_lines = project_file.readlines()

print(file_lines)

# create window
myWindow = arcade.open_window(800, 700, "Andrew Janedy Project 4")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# draw axis
arcade.draw_line(40, 700, 40, 40, arcade.color.BLACK)
arcade.draw_line(40, 40, 800, 40, arcade.color.BLACK)

# creating scale on y-axis
y_scale = (700 - 100) / len(range(100, 1400, 100))
current_y = 40

# draw legend
for i in range(100, 1600, 100):
    currentLabel = arcade.Text(f"{i}M", 5, current_y, arcade.color.BLACK, 8)
    currentLabel.draw()
    current_y += y_scale

nationsPop_contents = open("nationsPop.txt", 'r')
nationsPop_lines = nationsPop_contents.readlines()
list_length = len(nationsPop_lines)
current_x_value = (760/list_length)
current_line = 1

for current_country in nationsPop_lines:
    current_country = current_country.strip().split(",")
    bar_height = ((int(current_country[1])/100_000_000)*46.153847)
    if current_line % 2 == 1:
        country_label = arcade.Text(f"{current_country[0]}", current_x_value, 20, arcade.color.BLACK,
                                    8, 8, "center")
        if float(current_country[2]) >= 0:
            arcade.draw_line(current_x_value, 40, current_x_value, bar_height, arcade.color.BLUE,
                            760/(2*list_length))
        else:
            arcade.draw_line(current_x_value, 40, current_x_value, bar_height, arcade.color.RED,
                            760/(2*list_length))

    else:
        country_label = arcade.Text(f"{current_country[0]}", current_x_value, 30, arcade.color.BLACK,
                                    8, 8, "center")

        if float(current_country[2]) >= 0:
            arcade.draw_line(current_x_value, 40, current_x_value, bar_height, arcade.color.BLUE,
                             760 / (2 * list_length))
        else:
            arcade.draw_line(current_x_value, 40, current_x_value, bar_height, arcade.color.RED,
                             760 / (2 * list_length))

    country_label.draw()
    current_x_value += 760/list_length
    current_line += 1

arcade.finish_render()

arcade.run()