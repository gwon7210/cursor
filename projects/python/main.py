#####################
# Welcome to Cursor #
#####################

'''
Step 1: Try generating with Cmd+K or Ctrl+K on a new line. Ask for CLI-based game of TicTacToe.

Step 2: Hit Cmd+L or Ctrl+L and ask the chat what the code does. 
   - Then, try running the code

Step 3: Try highlighting all the code with your mouse, then hit Cmd+k or Ctrl+K. 
   - Instruct it to change the game in some way (e.g. add colors, add a start screen, make it 4x4 instead of 3x3)

Step 4: To try out cursor on your own projects, go to the file menu (top left) and open a folder.
'''
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("틱택토 게임")
        self.window.geometry("300x350")
        
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        # 게임 상태 표시 레이블
        self.status_label = tk.Label(
            self.window,
            text=f"플레이어 {self.current_player}의 차례",
            font=('Arial', 12)
        )
        self.status_label.pack(pady=10)
        
        # 게임 보드 프레임
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()
        
        # 버튼 생성
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
        
        # 재시작 버튼
        restart_button = tk.Button(
            self.window,
            text="게임 재시작",
            font=('Arial', 12),
            command=self.restart_game
        )
        restart_button.pack(pady=20)
        
    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row * 3 + col].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("게임 종료", f"플레이어 {self.current_player}가 이겼습니다!")
                self.restart_game()
            elif self.is_board_full():
                messagebox.showinfo("게임 종료", "무승부입니다!")
                self.restart_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"플레이어 {self.current_player}의 차례")
    
    def check_winner(self):
        # 가로 확인
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != " ":
                return True
        
        # 세로 확인
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True
        
        # 대각선 확인
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        
        return False
    
    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)
    
    def restart_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.status_label.config(text=f"플레이어 {self.current_player}의 차례")
        for button in self.buttons:
            button.config(text="")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
