def random(_num_of_faces: num, _input: num) -> num:
    # in case _faces == 6:
    # 1. slice [:5] of a numerical hash (6 digits)
    # 2. each digits represent a score for a _faces (0-9)
    # 3. the position with the high score is selected as
    #    result of the rolling dice.
    # For example [4, 6, 2, 8, 2, 4] -> face: 4
    # If the result is like this [4, 6, 8, 2, 5, 8]
    #    random take the first relative max value -> face: 3
    pass
