# Christmass-Tree
Hyperskill Project (https://hyperskill.org/projects/391?track=2)


Enter two numbers separated by space.

First number - number of tree lines (height of the tree)

Second number - tells which spot is filled with a decoration


Second Mode:
Objectives
The first objective is to create a postcard with width = 50 and height = 30.
The first and the last line contains symbols -.
Every other line starts and ends with the | symbol.
The X and Y axes position starts with 0. So, the left upper position of the symbol - is [0, 0], and the right bottom is [49, 29].
The line 27 contains the sentence Merry Xmas in the middle of the row.
The input may contain two numbers or a multiplication of four numbers.
If the input contains two numbers, print the Christmas tree as before. With a heigh equal to the first number and the interval of the decorations as the second number. The test checks the postcard mainly with the hash function, so it is strongly recommended to use the same function that prints the tree to use this function to put that tree on the postcard. On the other hand, the test script will not show exactly where the problem is with the tree.
If the input is a multiplication of four numbers, you should print a tree on the postcard in the way: H, I, L, C, where H is the height of the tree like before, I is an interval of decorations, L (Line) and C (Column) are coordinates when the top of the Christmas tree started (not the top of the tree ^ but the X on top). The number of trees may be higher than two.
The next tree printed on the postcard overlaps other trees.
