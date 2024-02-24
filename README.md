# Py2048

This repository contains a Python implementation of the popular 2048 game, built using PyQt5 for the graphical user interface.

## Overview

2048 is a single-player sliding block puzzle game. The game's objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. The game is won when a tile with the number 2048 appears on the board. The game is lost when there are no more moves possible to combine tiles.

## Features

- Sleek UI: Enjoy a modern interface with Qt5.
- Pythonic Logic: Experience the game's logic written entirely in Python.
- Intuitive Controls: Use arrow keys to smoothly maneuver tiles.
- Dark Mode: Play in style with a sleek dark mode theme.
- Quick Restart: Get back into the action with a one-click restart option.
- Notifications: Stay updated with clear win and game over notifications.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/Darshan-dlr/Py2048.git
    ```

2. Install dependencies:

    ```
    pip install PyQt5
    ```

## Usage

Run the main script to start the game:

```
python main.py
```

Use the arrow keys to move tiles on the game board. Combine tiles with the same number to reach 2048 and win the game. When no more moves are possible and the board is full, the game is over.

## File Structure

```
2048_game/
│
├── logic/
│   ├── __init__.py
│   └── logic.py
│
├── ui/
│   ├── __init__.py
│   └── ui.py
│
├── constants.py
└── main.py
```

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or create a pull request.
