import snakelib

width = 0  # initialized in play_snake
height = 0  # initialized in play_snake
ui = None  # initialized in play_snake
SPEED = 2
keep_running = True
x = 0
y = 0
key = 'r'
apple_x = 5
apple_y = 5

moves_list = [(0, 0), (1, 0)]
direction = 'r'

matrix_list = []

def first_apple():
    global apple_x, apple_y, moves_list, matrix_list

    number_free_spots = (width * height) - len(moves_list)

    for y_A in range(height):
        for x_A in range(width):
            matrix_list.append((x_A, y_A))

    for element in moves_list:  # moves_list = snake coordinates
        if element in matrix_list:  # matrix_list = grid
            matrix_list.pop(matrix_list.index(element))

    random_val = ui.random(number_free_spots)

    apple_x = matrix_list[random_val][0]
    apple_y = matrix_list[random_val][1]

    ui.place(apple_x, apple_y, ui.FOOD)


def add_apple():
    global apple_x, apple_y, moves_list, count, matrix_list

    matrix_list = []
    if apple_x == moves_list[-1][0] and apple_y == moves_list[-1][1]:


        for y_A in range(0, height):
            for x_A in range(0, width):
                matrix_list.append((x_A, y_A))

        number_free_spots = (width * height) - len(moves_list)


        for element in moves_list: # moves_list = snake coordinates
            if element in matrix_list:  # matrix_list = grid
                matrix_list.pop(matrix_list.index(element))

        random_val = ui.random(number_free_spots)

        apple_x = matrix_list[random_val][0]
        apple_y = matrix_list[random_val][1]

        ui.place(apple_x, apple_y, ui.FOOD)
    else:
        ui.place(apple_x, apple_y, ui.FOOD)


def control(event):
    global x, y, direction, apple_y, apple_x

    x = moves_list[-1][0]
    y = moves_list[-1][1]

    if event == 'l' and direction != 'r':

        if x <= 0:
            x = width - 1
        else:
            x -= 1

        direction = event

    if event == 'r' and direction != 'l':
        if x == width - 1:
            x = 0
        else:
            x += 1

        direction = event

    if event == 'u' and direction != 'd':
        if y <= 0:
            y = height - 1
        elif y <= height - 1:
            y -= 1

        direction = event


    if event == 'd' and direction != 'u':
        if y == height - 1:
            y = 0
        else:
            y += 1

        direction = event

    return x, y


def draw():
    # fill in draw code here

    global x, y, event, moves_list, key, prev_dir, direction


    ui.clear()

    add_apple()
    x, y = control(key)

    moves_list.append((x, y))
    if (moves_list[-1][0], moves_list[-1][1]) in moves_list[:-2]:
        if moves_list[-1] != moves_list[0]:
            ui.set_game_over()

    if (apple_x, apple_y) not in moves_list:
        moves_list.pop(0)


    if moves_list[-1][0] == apple_x and moves_list[-1][1] == apple_y:
        add_apple()


    for i in range(len(moves_list)):
        x_coo = moves_list[i][0]
        y_coo = moves_list[i][1]
        ui.place(x_coo, y_coo, ui.SNAKE)


    ui.show()


def play_snake(init_ui):
    global width, height, ui, keep_running, x, y, key, moves_list, direction
    ui = init_ui
    width, height = ui.board_size()

    ui.place(moves_list[0][0], moves_list[0][1], ui.SNAKE)
    ui.place(moves_list[1][0], moves_list[1][1], ui.SNAKE)
    first_apple()
    ui.show()


    while keep_running:
        # getting matrix_list

        event = ui.get_event()
        if event.name == "alarm":
            draw()

        if event.name == 'arrow':
            key = event.data


        # make sure you handle the quit event like below,
        # or the test might get stuck in an infinite loop

        elif event.name == "other" and event.data == "Return": #this is for the enter key
            #erase_everything()
            print(event.data)


        # make sure you handle the quit event like below,
        # or the test might get stuck in an infinite loop
        if event.name == "quit":
            keep_running = False

        if event.name == "quit":
            keep_running = False



if __name__ == "__main__":
    # do this if running this module directly
    # (not when importing it for the tests)
    ui = snakelib.SnakeUserInterface(10, 10)
    ui.set_animation_speed(SPEED)
    play_snake(ui)
