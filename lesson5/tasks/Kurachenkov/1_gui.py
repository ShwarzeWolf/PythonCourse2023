import random
import time
import tkinter as tk
import threading

class GameOfLifeGUI:
    def __init__(self, root, n, m):
        self.root = root
        self.n = n
        self.m = m
        self.board = self._create_board()
        self.prev_boards = []

        self.canvas = tk.Canvas(root, width=n*20, height=m*20)
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

        self.game_running = False
        self.game_thread = None

    def _create_board(self):
        return [[random.randint(0, 1) for i in range(self.m)] for j in range(self.n)]

    def _draw_board(self):
        self.canvas.delete("all")
        for i in range(self.n):
            for j in range(self.m):
                color = "black" if self.board[i][j] == 1 else "white"
                self.canvas.create_rectangle(i*20, j*20, (i+1)*20, (j+1)*20, fill=color)

    def _get_next_state(self):
        new_board = [[0 for i in range(self.m)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                live_neighbors = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x == 0 and y == 0:
                            continue
                        if i + x < 0 or i + x >= self.n or j + y < 0 or j + y >= self.m:
                            continue
                        if self.board[i + x][j + y] == 1:
                            live_neighbors += 1
                if self.board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = 1
                else:
                    if live_neighbors == 3:
                        new_board[i][j] = 1
                    else:
                        new_board[i][j] = 0
        return new_board

    def _is_game_over(self):
        flat_board = [cell for row in self.board for cell in row]
        flat_prev_boards = [[cell for row in prev_board for cell in row] for prev_board in self.prev_boards]
        if sum(flat_board) == 0 or flat_board in flat_prev_boards:
            print("Game over!")
            return True
        return False

    def update_game(self):
        while not self._is_game_over() and self.game_running:
            self._draw_board()
            self.prev_boards.append([row[:] for row in self.board])
            self.board = self._get_next_state()
            self.root.update()
            time.sleep(1)

    def start_game(self):
        if not self.game_running:
            self.game_running = True
            self.game_thread = threading.Thread(target=self.update_game)
            self.game_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    game = GameOfLifeGUI(root, 10, 10)
    root.mainloop()
