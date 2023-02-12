from src.entities.game import Game
from src.entities.board import Board
from src.visualization.colorsEnum import Color, Positions
import numpy as np
import matplotlib.pyplot as plt

WIDTH = 20
HEIGHT = 20


class MatplotlibVisualize:

    def __init__(self):
        self.board = None

    def visualize_board(self, board):
        """
        Visualize actual state of the board
        :board: Board to visualize
        :returns matplotlib plot
        """
        self.board = board
        grid = self.create_default_grid()
        self.visualize_grid(grid)

    def visualize_grid(self, grid):
        """
        Visualize given grid
        :param grid: grid to plot
        """
        plt.figure()
        im = plt.imshow(grid, interpolation="none")
        ax = plt.gca()
        ax.set_xticks(np.arange(0, WIDTH, 1))
        ax.set_yticks(np.arange(0, HEIGHT, 1))
        # Labels for major ticks
        ax.set_xticklabels(np.arange(0, WIDTH, 1))
        ax.set_yticklabels(np.arange(0, HEIGHT, 1))

        # Minor ticks
        ax.set_xticks(np.arange(-.5, WIDTH, 1), minor=True)
        ax.set_yticks(np.arange(-.5, HEIGHT, 1), minor=True)

        # Gridlines based on minor ticks
        ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

        # Remove minor ticks
        ax.tick_params(which='minor', bottom=False, left=False)
        ax.grid(which='minor', color='black', linestyle='-', linewidth=1)
        plt.show()

    def create_default_grid(self) -> list:
        """
        Creates default grid
        :return: game baord grid
        """
        grid = np.ones((HEIGHT, WIDTH, 3), dtype=np.int8) * 156
        grid[1:3, 1:3] = Color.PAWN_GREEN.value
        grid[8, 1:8] = Color.GREEN.value
        grid[10, 1:8] = Color.GREEN.value
        grid[8:10, 1] = Color.GREEN.value
        grid[9, 3:7] = Color.LIGHT_GREEN.value
        grid[8, 1] = Color.LIGHT_GREEN.value

        grid[16:18, 1:3] = Color.PAWN_YELLOW.value
        grid[17, 8:11] = Color.YELLOW.value
        grid[11:18, 8] = Color.YELLOW.value
        grid[11:18, 10] = Color.YELLOW.value
        grid[12:16, 9] = Color.LIGHT_YELLOW.value
        grid[17, 8] = Color.LIGHT_YELLOW.value

        grid[1:3, 16:18] = Color.PAWN_RED.value
        grid[1, 8:11] = Color.RED.value
        grid[1:8, 8] = Color.RED.value
        grid[1:8, 10] = Color.RED.value
        grid[3:7, 9] = Color.LIGTH_RED.value
        grid[1, 10] = Color.LIGTH_RED.value

        grid[16:18, 16:18] = Color.PAWN_BLUE.value
        grid[8, 11:18] = Color.BLUE.value
        grid[10, 11:18] = Color.BLUE.value
        grid[8:10, 17] = Color.BLUE.value
        grid[9, 12:16] = Color.LIGHT_BLUE.value
        grid[10, 17] = Color.LIGHT_BLUE.value

        grid[:, 19] = Color.SPACE_COLOR.value
        grid = self.map_game_board(grid)
        return grid

    def map_game_board(self, grid):
        current_board = self.board
        for field, coords in zip(current_board.fields, Positions):
            if field.pawns:
                pawn_color = "PAWN_" + field.pawns[0].color
                grid[coords.value] = getattr(Color, pawn_color).value
        return grid


viz = MatplotlibVisualize()
game = Game(seed=3222)
for i in range(32):
    game.move()
board = game.board
viz.visualize_board(board)