#!/usr/bin/python3
#coding:utf-8

import random

import constants as c

def initialize_game():
    """
    Initializes a new game matrix with two random numbers.

    :return: The initial game matrix.
    :rtype: list
    """
    matrix = [[0] * c.GRID_SIZE for _ in range(c.GRID_SIZE)]
    add_random_number(matrix)
    add_random_number(matrix)
    return matrix

def add_random_number(matrix):
    """
    Adds a random number (either 2 or 4) to a random empty cell in the matrix.

    :param matrix: The game matrix to add a random number to.
    :type matrix: list
    :return: The updated game matrix after adding the random number.
    :rtype: list
    """
    empty_cells = [(i, j) for i in range(c.GRID_SIZE) for j in range(c.GRID_SIZE) if matrix[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        matrix[i][j] = 2 if random.random() < 0.9 else 4
    return matrix

def merge_tiles(row):
    """
    Merges identical tiles in a row.

    :param row: The row to merge tiles in.
    :type row: list
    :return: The row after merging tiles.
    :rtype: list
    """
    new_row = [val for val in row if val != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [val for val in new_row if val != 0]
    return new_row + [0] * (len(row) - len(new_row))

def move_left(matrix):
    """
    Moves all tiles to the left and merges identical tiles that collide.

    :param matrix: The game matrix to move left.
    :type matrix: list
    :return: The game matrix after moving left.
    :rtype: list
    """
    new_matrix = [merge_tiles(row) for row in matrix]
    return new_matrix

def move_right(matrix):
    """
    Moves all tiles to the right and merges identical tiles that collide.

    :param matrix: The game matrix to move right.
    :type matrix: list
    :return: The game matrix after moving right.
    :rtype: list
    """
    new_matrix = [list(reversed(row)) for row in matrix]
    new_matrix = [merge_tiles(row) for row in new_matrix]
    new_matrix = [list(reversed(row)) for row in new_matrix]
    return new_matrix

def move_up(matrix):
    """
    Moves all tiles up and merges identical tiles that collide.

    :param matrix: The game matrix to move up.
    :type matrix: list
    :return: The game matrix after moving up.
    :rtype: list
    """
    transposed = [list(row) for row in zip(*matrix)]
    new_matrix = [merge_tiles(row) for row in transposed]
    new_matrix = [list(row) for row in zip(*new_matrix)]
    return new_matrix

def move_down(matrix):
    """
    Moves all tiles down and merges identical tiles that collide.

    :param matrix: The game matrix to move down.
    :type matrix: list
    :return: The game matrix after moving down.
    :rtype: list
    """
    transposed = [list(row) for row in zip(*matrix)]
    new_matrix = [list(reversed(row)) for row in transposed]
    new_matrix = [merge_tiles(row) for row in new_matrix]
    new_matrix = [list(reversed(row)) for row in new_matrix]
    new_matrix = [list(row) for row in zip(*new_matrix)]
    return new_matrix

def is_game_over(matrix):
    """
    Checks if the game is over.

    :param matrix: The game matrix to check.
    :type matrix: list
    :return: True if the game is over, False otherwise.
    :rtype: bool
    """
    for row in matrix:
        if 0 in row:
            return False
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                return False
    transposed = [list(row) for row in zip(*matrix)]
    for row in transposed:
        if 0 in row:
            return False
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                return False
    return True

def is_game_won(matrix):
    """
    Checks if the game is won by reaching 2048.

    :param matrix: The game matrix to check.
    :type matrix: list
    :return: True if the game is won, False otherwise.
    :rtype: bool
    """
    return any(any(cell == 2048 for cell in row) for row in matrix)
