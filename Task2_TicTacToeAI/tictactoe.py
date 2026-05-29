import math

board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[pos] == player for pos in combo) for combo in win_positions)

def is_draw():
    return ' ' not in board

def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):
        return 1
    if check_winner(b, 'X'):
        return -1
    if ' ' not in b:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    board[move] = 'O'

def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position!")
            elif board[move] != ' ':
                print("Position already occupied!")
            else:
                board[move] = 'X'
                break

        except ValueError:
            print("Please enter a number between 1 and 9.")

def main():
    print("=== TIC TAC TOE AI ===")
    print("You = X")
    print("AI = O")
    print("""
Positions:

1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
""")

    while True:
        print_board()
        player_move()

        if check_winner(board, 'X'):
            print_board()
            print("You Win!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

        ai_move()

        if check_winner(board, 'O'):
            print_board()
            print("AI Wins!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

if __name__ == "__main__":
    main()