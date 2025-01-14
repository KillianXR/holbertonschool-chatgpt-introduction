#!/usr/bin/python3

def print_board(board):
    """Affiche le plateau de jeu."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Vérifie si un joueur a gagné."""
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie la diagonale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Vérifie l'autre diagonale
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Exécute le jeu Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        # Demande les entrées de l'utilisateur avec validation
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                # Vérifie si les entrées sont valides
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid input. Row and column must be between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break  # Si tout est valide, sort de la boucle
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        # Place le marqueur sur le plateau
        board[row][col] = player
        
        # Vérifie si un joueur a gagné
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Change de joueur
        player = "O" if player == "X" else "X"

# Exécution du jeu
tic_tac_toe()
