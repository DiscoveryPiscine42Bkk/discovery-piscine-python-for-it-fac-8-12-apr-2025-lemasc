# begin: utils

class ANSI:
    """
    ANSI codes for console color output
    See: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    """
    DEFAULT = '\033[0m'
    # Styles
    HIGHLIGHTED_RED = '\033[41m'
    HIGHLIGHTED_GREEN = '\033[42m'
    HIGHLIGHTED_YELLOW = '\033[43m'
    HIGHLIGHTED_BLUE = '\033[44m'
    HIGHLIGHTED_PURPLE = '\033[45m'
    HIGHLIGHTED_CYAN = '\033[46m'
    HIGHLIGHTED_GREY = '\033[47m'
    BLACK_LIGHT = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'


def print_with_color(values, color, end="\n"):
  """
  Print a string with a specific color
  """
  if color:
    print("%s%s%s" % (color, values, ANSI.DEFAULT), end=end)
  else:
    print("%s%s" % (values, ANSI.DEFAULT), end=end)

# end: utils
# begin: checkmate

def is_area_pawn(row: int, column: int, center_i: int, center_j: int):
    return (
        center_i - row == 1 and
        abs(center_j - column) == 1
    )

def is_area_bishop(row: int, column: int, center_i: int, center_j: int):
    return abs(center_i - row) == abs(center_j - column)

def is_area_rook(row: int, column: int, center_i: int, center_j: int):
    return center_i == row or center_j == column


def is_area_queen(row: int, column: int, center_i: int, center_j: int):
    a = abs(center_i - row) == abs(center_j - column)
    b = center_i == row or center_j == column
    return (a or b)

def is_king_in_range(board, initial_point, check_fn):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "K" and check_fn(i, j, initial_point[0], initial_point[1]):
                return True
    return False

check_fn_by_cell = {
    "P": is_area_pawn,
    "B": is_area_bishop,
    "R": is_area_rook,
    "Q": is_area_queen,
}

def checkmate(board):
    success = False
    b = board.split("\n")
    for i in range(len(b)):
        for j in range(len(b[i])):
            cell = b[i][j]
            if cell == "K":
                print_with_color(cell, color=ANSI.HIGHLIGHTED_RED, end=" ")
                continue
            if cell in check_fn_by_cell and is_king_in_range(b, (i, j), check_fn_by_cell[cell]):
                print_with_color(cell, color=ANSI.HIGHLIGHTED_CYAN, end=" ")
                success = True
                continue
            print_with_color(cell, end=" ", color=ANSI.WHITE if cell == "K" else ANSI.BLACK_LIGHT)
        print()
    print("Success! King In Check!" if success else "King not in check.")