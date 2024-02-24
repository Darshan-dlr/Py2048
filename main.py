#!/usr/bin/python3
#coding:utf-8

from PyQt5.QtWidgets import QApplication

from ui.ui import Game2048

def main():
    app = QApplication([])
    game = Game2048()
    game.show()
    app.exec_()

if __name__ == "__main__":
    main()
