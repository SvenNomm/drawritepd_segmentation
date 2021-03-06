def test_names():
    test_list = []
    test_list.append('plcontinue')
    test_list.append('plcopy')
    test_list.append('pltrace')

    test_list.append('pcontinue')
    test_list.append('pcopy')
    test_list.append('ptrace')
    test_list.append('spiral')
    return test_list


def test_name_latex():
    test_name = []
    test_name.append('$\Pi \Lambda $ continue')
    test_name.append('$\Pi \Lambda $ copy')
    test_name.append('$\Pi \Lambda $ trace')

    test_name.append('$\Pi $ continue')
    test_name.append('$\Pi $ copy')
    test_name.append('$\Pi $ trace')
    return test_name


def screen_resolution():
    screen_x_max = 1024
    screen_y_max = 768
    return screen_x_max, screen_y_max


def screen_size():
    screen_x_max_mm = 198
    screen_y_max_mm = 149
    return screen_x_max_mm, screen_y_max_mm


def pixel_properties():
    x_mm2pix = 5.17
    y_mm2pix = 5.15
    return x_mm2pix, y_mm2pix

def spiral_parameters():
    # the following parameters were found experimentally for iPad version
    a = 1.4
    b = 8
    angle_0 = 0
    angle_1 = 11.32 * 3.14# alternatively import numpy and call value pi
    return a, b, angle_0, angle_1
