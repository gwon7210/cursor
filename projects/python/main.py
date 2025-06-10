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
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # 가로 확인
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]
    
    # 세로 확인
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def show_start_screen():
    print("=" * 40)
    print("           틱택토 게임에 오신 것을 환영합니다!")
    print("=" * 40)
    print("\n게임 규칙:")
    print("1. 두 명의 플레이어가 번갈아가며 X와 O를 표시합니다.")
    print("2. 3x3 보드에서 가로, 세로, 또는 대각선으로 같은 표시를 먼저 완성하면 승리합니다.")
    print("3. 1-9 사이의 숫자를 입력하여 원하는 위치에 표시를 합니다.")
    print("\n보드 위치:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("\n게임을 시작하려면 Enter 키를 누르세요...")
    input()

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    show_start_screen()
    print("\n게임을 시작합니다!")
    
    while True:
        print_board(board)
        
        try:
            position = int(input(f"플레이어 {current_player}의 차례입니다. 위치를 선택하세요 (1-9): ")) - 1
            row = position // 3
            col = position % 3
            
            if position < 0 or position > 8:
                print("1-9 사이의 숫자를 입력하세요!")
                continue
                
            if board[row][col] != " ":
                print("이미 선택된 위치입니다!")
                continue
                
            board[row][col] = current_player
            
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"플레이어 {winner}가 이겼습니다!")
                break
                
            if is_board_full(board):
                print_board(board)
                print("무승부입니다!")
                break
                
            current_player = "O" if current_player == "X" else "X"
            
        except ValueError:
            print("올바른 숫자를 입력하세요!")

if __name__ == "__main__":
    main()
