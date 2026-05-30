#!/usr/bin/env python3
"""
Simple Tetris implemented with Tkinter (no external dependencies).
Controls:
  ← → : Move left/right
  ↓   : Soft drop
  ↑ / X : Rotate clockwise
  Z   : Rotate counter-clockwise
  Space : Hard drop
  C   : Hold piece
  P   : Pause
  R   : Restart
"""

import tkinter as tk
import random
from typing import List, Tuple, Optional

# Game constants
COLS = 10
ROWS = 20
CELL_SIZE = 30
BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE

# Tetromino shapes (standard SRS)
SHAPES = {
    'I': [(0, 1), (1, 1), (2, 1), (3, 1)],
    'O': [(0, 0), (1, 0), (0, 1), (1, 1)],
    'T': [(1, 0), (0, 1), (1, 1), (2, 1)],
    'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
    'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
    'J': [(0, 0), (0, 1), (1, 1), (2, 1)],
    'L': [(2, 0), (0, 1), (1, 1), (2, 1)],
}
aa = "#7400f0"
# Colors
COLORS = {
    'I': '#00f0f0',
    'O': '#f0f000',
    'T': '#a000f0',
    'S': '#00f000',
    'Z': '#f00000',
    'J': '#0000f0',
    'L': '#f0a000',
    'ghost': '#555555',
}

# Wall kick data (simplified SRS for 90° rotations)
WALL_KICKS = {
    'normal': [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
    'I': [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)],
}

class Tetris:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tetris")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            root, 
            width=BOARD_WIDTH + 120, 
            height=BOARD_HEIGHT + 40,
            bg="#111111",
            highlightthickness=0
        )
        self.canvas.pack(padx=10, pady=10)

        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.current_piece: Optional[dict] = None
        self.hold_piece: Optional[str] = None
        self.hold_used = False
        self.next_pieces: List[str] = []
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.drop_interval = 1000  # ms
        self.game_over = False
        self.paused = False

        self._init_pieces()
        self._spawn_piece()
        self._draw()

        # Key bindings
        self.root.bind("<Left>", lambda e: self._move(-1, 0))
        self.root.bind("<Right>", lambda e: self._move(1, 0))
        self.root.bind("<Down>", lambda e: self._soft_drop())
        self.root.bind("<Up>", lambda e: self._rotate(1))
        self.root.bind("x", lambda e: self._rotate(1))
        self.root.bind("z", lambda e: self._rotate(-1))
        self.root.bind("<space>", lambda e: self._hard_drop())
        self.root.bind("c", lambda e: self._hold())
        self.root.bind("p", lambda e: self._toggle_pause())
        self.root.bind("r", lambda e: self._restart())
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self._game_loop()

    def _init_pieces(self):
        """Initialize the bag of 7 pieces (random bag system)."""
        self.next_pieces = []
        self._refill_bag()

    def _refill_bag(self):
        bag = list(SHAPES.keys())
        random.shuffle(bag)
        self.next_pieces.extend(bag)

    def _get_next_piece(self) -> str:
        if len(self.next_pieces) < 7:
            self._refill_bag()
        return self.next_pieces.pop(0)

    def _spawn_piece(self):
        """Spawn a new tetromino at the top."""
        if not self.next_pieces:
            self._refill_bag()

        shape = self._get_next_piece()
        self.current_piece = {
            "shape": shape,
            "x": COLS // 2 - 1,
            "y": 0,
            "rotation": 0
        }

        if self._check_collision():
            self.game_over = True

        self.hold_used = False

    def _get_piece_cells(self, piece: dict) -> List[Tuple[int, int]]:
        """Get absolute board coordinates of the current piece."""
        shape = SHAPES[piece["shape"]]
        cells = []
        cx, cy = piece["x"], piece["y"]

        for dx, dy in shape:
            # Simple rotation (no full SRS matrix for brevity, but works for most cases)
            if piece["rotation"] % 4 == 0:
                rx, ry = dx, dy
            elif piece["rotation"] % 4 == 1:
                rx, ry = -dy, dx
            elif piece["rotation"] % 4 == 2:
                rx, ry = -dx, -dy
            else:
                rx, ry = dy, -dx
            cells.append((cx + rx, cy + ry))
        return cells

    def _check_collision(self, dx=0, dy=0, drot=0, piece=None) -> bool:
        """Check if moving/rotating the piece would cause a collision."""
        if piece is None:
            piece = self.current_piece
        if piece is None:
            return True

        temp = piece.copy()
        temp["x"] += dx
        temp["y"] += dy
        temp["rotation"] = (temp["rotation"] + drot) % 4

        cells = self._get_piece_cells(temp)
        for x, y in cells:
            if x < 0 or x >= COLS or y >= ROWS:
                return True
            if y >= 0 and self.board[y][x] is not None:
                return True
        return False

    def _lock_piece(self):
        """Lock the current piece into the board."""
        cells = self._get_piece_cells(self.current_piece)
        shape = self.current_piece["shape"]
        for x, y in cells:
            if 0 <= y < ROWS:
                self.board[y][x] = shape

        lines = self._clear_lines()
        if lines > 0:
            self._add_score(lines)

        self._spawn_piece()

    def _clear_lines(self) -> int:
        """Clear full lines and return how many were cleared."""
        new_board = [row for row in self.board if any(cell is None for cell in row)]
        lines_cleared = ROWS - len(new_board)
        while len(new_board) < ROWS:
            new_board.insert(0, [None] * COLS)
        self.board = new_board
        self.lines_cleared += lines_cleared
        return lines_cleared

    def _add_score(self, lines: int):
        points = {1: 100, 2: 300, 3: 500, 4: 800}
        self.score += points.get(lines, 0) * self.level
        self.level = 1 + self.lines_cleared // 10
        self.drop_interval = max(100, 1000 - (self.level - 1) * 50)

    def _move(self, dx: int, dy: int):
        if self.game_over or self.paused or not self.current_piece:
            return
        if not self._check_collision(dx, dy):
            self.current_piece["x"] += dx
            self.current_piece["y"] += dy
            self._draw()

    def _rotate(self, direction: int):
        if self.game_over or self.paused or not self.current_piece:
            return
        for kick in [0, -1, 1, -2, 2]:
            if not self._check_collision(0, 0, direction):
                self.current_piece["rotation"] = (self.current_piece["rotation"] + direction) % 4
                self._draw()
                return
            # Simple wall kick attempt
            if not self._check_collision(kick, 0, direction):
                self.current_piece["x"] += kick
                self.current_piece["rotation"] = (self.current_piece["rotation"] + direction) % 4
                self._draw()
                return

    def _soft_drop(self):
        if self.game_over or self.paused or not self.current_piece:
            return
        if not self._check_collision(0, 1):
            self.current_piece["y"] += 1
            self.score += 1  # soft drop points
            self._draw()
        else:
            self._lock_piece()
            self._draw()

    def _hard_drop(self):
        if self.game_over or self.paused or not self.current_piece:
            return
        drop_distance = 0
        while not self._check_collision(0, 1):
            self.current_piece["y"] += 1
            drop_distance += 1
        self.score += drop_distance * 2
        self._lock_piece()
        self._draw()

    def _hold(self):
        if self.game_over or self.paused or not self.current_piece or self.hold_used:
            return

        current_shape = self.current_piece["shape"]
        if self.hold_piece is None:
            self.hold_piece = current_shape
            self._spawn_piece()
        else:
            self.current_piece = {
                "shape": self.hold_piece,
                "x": COLS // 2 - 1,
                "y": 0,
                "rotation": 0
            }
            self.hold_piece = current_shape

        self.hold_used = True
        self._draw()

    def _toggle_pause(self):
        if self.game_over:
            return
        self.paused = not self.paused
        self._draw()

    def _restart(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.current_piece = None
        self.hold_piece = None
        self.hold_used = False
        self.next_pieces = []
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.drop_interval = 1000
        self.game_over = False
        self.paused = False
        self._init_pieces()
        self._spawn_piece()
        self._draw()

    def _game_loop(self):
        if self.game_over or self.paused:
            self.root.after(100, self._game_loop)
            return

        if not self._check_collision(0, 1):
            self.current_piece["y"] += 1
        else:
            self._lock_piece()

        self._draw()
        self.root.after(self.drop_interval, self._game_loop)

    def _draw(self):
        self.canvas.delete("all")

        # Draw board
        for y in range(ROWS):
            for x in range(COLS):
                if self.board[y][x]:
                    color = COLORS[self.board[y][x]]
                    self._draw_cell(x, y, color)

        # Draw current piece
        if self.current_piece:
            cells = self._get_piece_cells(self.current_piece)
            for x, y in cells:
                if y >= 0:
                    self._draw_cell(x, y, COLORS[self.current_piece["shape"]])

            # Ghost piece
            ghost = self.current_piece.copy()
            while not self._check_collision(0, 1, piece=ghost):
                ghost["y"] += 1
            for x, y in self._get_piece_cells(ghost):
                if y >= 0:
                    self._draw_cell(x, y, COLORS["ghost"], outline=True)

        # Draw next piece
        if self.next_pieces:
            next_shape = self.next_pieces[0]
            self.canvas.create_text(BOARD_WIDTH + 60, 30, text="NEXT", fill="white", font=("Helvetica", 14, "bold"))
            for dx, dy in SHAPES[next_shape]:
                self._draw_cell(COLS + dx, dy + 2, COLORS[next_shape], offset=True)

        # Hold piece
        self.canvas.create_text(BOARD_WIDTH + 60, 120, text="HOLD", fill="white", font=("Helvetica", 14, "bold"))
        if self.hold_piece:
            for dx, dy in SHAPES[self.hold_piece]:
                self._draw_cell(COLS + dx, dy + 5, COLORS[self.hold_piece], offset=True)

        # Score
        self.canvas.create_text(BOARD_WIDTH + 60, 200, text="SCORE", fill="white", font=("Helvetica", 12))
        self.canvas.create_text(BOARD_WIDTH + 60, 220, text=str(self.score), fill="white", font=("Helvetica", 16, "bold"))
        self.canvas.create_text(BOARD_WIDTH + 60, 250, text=f"LEVEL {self.level}", fill="#aaa", font=("Helvetica", 12))

        if self.paused:
            self.canvas.create_text(BOARD_WIDTH // 2, BOARD_HEIGHT // 2, 
                                   text="PAUSED", fill="white", font=("Helvetica", 24, "bold"))
        if self.game_over:
            self.canvas.create_text(BOARD_WIDTH // 2, BOARD_HEIGHT // 2, 
                                   text="GAME OVER", fill="#ff4444", font=("Helvetica", 24, "bold"))
            self.canvas.create_text(BOARD_WIDTH // 2, BOARD_HEIGHT // 2 + 30, 
                                   text="Press R to restart", fill="#aaa", font=("Helvetica", 14))

    def _draw_cell(self, x: int, y: int, color: str, offset: bool = False, outline: bool = False):
        px = x * CELL_SIZE + (20 if offset else 0)
        py = y * CELL_SIZE + 20
        self.canvas.create_rectangle(0, 20, CELL_SIZE*10, CELL_SIZE*20 + 20, 
                                    fill="", outline=COLORS["ghost"], width=1)
        self.canvas.create_rectangle(0, 20, CELL_SIZE*10, 20, 
                                    fill="", outline="#000000", width=1)
        if outline:
            self.canvas.create_rectangle(px, py, px + CELL_SIZE+1, py + CELL_SIZE, 
                                        fill="", outline=color, width=1)
        else:
            self.canvas.create_rectangle(px + 1, py + 1, px + CELL_SIZE - 1, py + CELL_SIZE - 1, 
                                        fill=color, outline="#222")


def main():
    root = tk.Tk()
    Tetris(root)
    root.mainloop()


if __name__ == "__main__":
    main()