
"""
To print in spiral form a given array of dimensions (i, j):

CONSIDERATIONS: We can go on four directions: right-to-left, left-to-right, top-to-bottom and bottom-to-top.
    (indexes analysis)
    int top = 0; bottom = amount_of_rows - 1; left = 0, right = amount_of_columns - 1;

    (0)left-to-right -> [constant][increasing]
    (1)top-to-bottom -> [increasing][constant]
    (2)right-to-left -> [constant][decreasing]
    (3)bottom-to-top -> [decreasing][constant]

It's better to use ifs instead of whiles due to the amount of information that has to be updated in every new loop. Plus... There's still a bug I need to solve.

"""
Minding the above instructions, I coded my code.