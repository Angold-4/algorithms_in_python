# Ruler Angold4 20200611
def draw_line(tick_length, tick_label=''):
    """draw a new line with given length and option label"""
    line = '-'*tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """use recursive method to draw the things between two label line"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    """main function which draw a ruler with given inches and given accuary"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


if __name__ == "__main__":
    draw_ruler(3, 5)

    """
    ----- 0
    -
    --
    -
    ---
    -
    --
    -
    ----
    -
    --
    -
    ---
    -
    --
    -
    ----- 1
    -
    --
    -
    ---
    -
    --
    -
    ----
    -
    --
    -
    ---
    -
    --
    -
    ----- 2
    -
    --
    -
    ---
    -
    --
    -
    ----
    -
    --
    -
    ---
    -
    --
    -
    ----- 3
    """
