class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # Step 1: Find the position of the white Rook ('R')
        rook_r, rook_c = -1, -1
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rook_r, rook_c = r, c
                    break
            if rook_r != -1:
                break

        captures = 0
        # Directions: (row_change, col_change) -> Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Search in all 4 cardinal directions
        for dr, dc in directions:
            r, c = rook_r + dr, rook_c + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'B':  # Friendly bishop blocks the way
                    break
                if board[r][c] == 'p':  # Enemy pawn captured
                    captures += 1
                    break
                r += dr
                c += dc

        return captures
        