def knightsTour(rows, cols):
    def is_valid_move(x, y, board):
        return 0 <= x < rows and 0 <= y < cols and board[x][y] == -1

    def solve(x, y, move_count):
        if move_count == rows * cols:
            return True
        
        moves = sorted(
            [(x + dx, y + dy) for dx, dy in moveset],
            key=lambda move: sum(is_valid_move(move[0] + dx, move[1] + dy, board) for dx, dy in moveset)
        )
        
        for nx, ny in moves:
            if is_valid_move(nx, ny, board):
                board[nx][ny] = move_count
                if solve(nx, ny, move_count + 1):
                    return True
                board[nx][ny] = -1
        
        return False
    
    moveset = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    for start_x in range(rows):
        for start_y in range(cols):
            board = [[-1] * cols for _ in range(rows)]
            board[start_x][start_y] = 0
            if solve(start_x, start_y, 1):
                return board
    
    return None

print(knightsTour(5,5))