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

def check_and_parse_board(board: str):
  rows = board.upper().split("\n")
  row_n = len(rows)

  if row_n < 2:
    print_with_color("[error]", color=ANSI.RED, end=" ")
    print(f"Board size must be at least 2x2, you provided only {row_n} row.")
    return None

  for i in range(row_n):
    col_n = len(rows[i])
    if row_n != col_n:
        print_with_color("[error]", color=ANSI.RED, end=" ")
        print(f"Row {i + 1} has {col_n} column{"s" if col_n > 1 else ""}, expected board square size ({row_n}x{row_n})")
        return None
    for j in range(col_n):
       if rows[i][j] not in ".KPBRQ":
          rows[i][j] = "."
  return rows

def is_area_pawn(row: int, column: int, center_i: int, center_j: int):
    if (center_i - row == 1 and abs(center_j - column) == 1):
        return 1

def is_area_bishop(row: int, column: int, center_i: int, center_j: int):
    a = abs(center_i - row)
    b = abs(center_j - column)
    if (a == b):
       return a

def is_area_rook(row: int, column: int, center_i: int, center_j: int):
    if (center_i == row or center_j == column):
       return max(abs(center_i - row), abs(center_j - column))

def is_area_queen(row: int, column: int, center_i: int, center_j: int):
    a = abs(center_i - row) == abs(center_j - column)
    b = center_i == row or center_j == column
    return (a or b)

def get_notation(row: int, column: int):
    """
    Convert a row and column to chess notation
    """
    return f"{chr(column + 65)}{row + 1}"


def is_king_in_range(board, initial_point, check_fn):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "K":
                delta = check_fn(i, j, initial_point[0], initial_point[1])
                if delta:
                   return delta
    return False

check_fn_by_cell = {
    "P": is_area_pawn,
    "B": is_area_bishop,
    "R": is_area_rook,
    "Q": is_area_queen,
}

def checkmate(board):
    captured = {}
    success = False
    b = check_and_parse_board(board)
    if b:
        for i in range(len(b)):
            for j in range(len(b[i])):
                cell = b[i][j]
                if cell == "K":
                    print_with_color(cell, color=ANSI.HIGHLIGHTED_RED, end=" ")
                    continue
                if cell in check_fn_by_cell:
                    delta = is_king_in_range(b, (i, j), check_fn_by_cell[cell])
                    if delta:
                        print_with_color(cell, color=ANSI.HIGHLIGHTED_CYAN, end=" ")
                        if not captured.get(delta):
                            captured[delta] = []
                        captured[delta].append((i, j))
                        success = True
                    continue
                print_with_color(cell, end=" ", color=ANSI.WHITE if cell == "K" else ANSI.BLACK_LIGHT)
            print()
    for least_delta in sorted(captured.keys()):
        print(f"King is in check by {least_delta} from", end=": ")
        for cell in captured[least_delta]:
            i = cell[0]
            j = cell[1]
            print_with_color(f"{get_notation(i, j)}", color=ANSI.YELLOW, end=" ")
            print(f"({b[i][j]})", end=" ")
        print()
    print("Success" if success else "Fail")
    return success