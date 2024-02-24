#!/usr/bin/python3
#coding:utf-8

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import Qt

import constants as c
from logic import logic

class Game2048(QMainWindow):
    """
    Main window class for the 2048 game.
    """
    def __init__(self):
        """
        Initializes the game window.
        """
        super().__init__()

        self.initUI()

        self.matrix = logic.initialize_game()
        self.update_ui()

    def initUI(self):
        """
        Sets up the user interface.
        """
        self.setWindowTitle("2048")
        self.setGeometry(100, 100, c.WINDOW_SIZE, c.WINDOW_SIZE)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)
        self.central_widget.setLayout(self.grid_layout)

    def keyPressEvent(self, event):
        """
        Handles key press events for moving tiles.

        :param event: The key press event.
        :type event: QKeyEvent
        """
        key = event.key()
        moved = False
        if key == Qt.Key_Left:
            self.matrix = logic.move_left(self.matrix)
            moved = True
        elif key == Qt.Key_Right:
            self.matrix = logic.move_right(self.matrix)
            moved = True
        elif key == Qt.Key_Up:
            self.matrix = logic.move_up(self.matrix)
            moved = True
        elif key == Qt.Key_Down:
            self.matrix = logic.move_down(self.matrix)
            moved = True

        if moved:
            self.matrix = logic.add_random_number(self.matrix)
            self.update_ui()

            if logic.is_game_won(self.matrix):
                self.show_message("You Win!")
            elif logic.is_game_over(self.matrix):
                self.game_over_message()

    def update_ui(self):
        """
        Updates the user interface to reflect the current game state.
        """
        for i in range(c.GRID_SIZE):
            for j in range(c.GRID_SIZE):
                cell_value = self.matrix[i][j]
                label = QLabel(str(cell_value) if cell_value != 0 else "")
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet(f"background-color: {c.CELL_COLORS.get(cell_value, c.EMPTY_CELL_COLOR)}; color: black; font-family: {c.FONT_FAMILY}; font-size: {c.FONT_SIZE}px;")
                self.grid_layout.addWidget(label, i, j)

    def show_message(self, message):
        """
        Shows a message box with the specified message.

        :param message: The message to display.
        :type message: str
        """
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.exec_()

    def game_over_message(self):
        """
        Displays a game over message box and prompts the user to restart or quit the game.
        """
        reply = QMessageBox.question(self, 'Game Over', 'Game Over! Do you want to restart?', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.restart_game()
        else:
            QApplication.quit()

    def restart_game(self):
        """
        Restarts the game by initializing a new game matrix and updating the UI.
        """
        self.matrix = logic.initialize_game()
        self.update_ui()

if __name__ == '__main__':
    app = QApplication([])
    game = Game2048()
    game.show()
    app.exec_()
