from pyscript import document

# ==========================================
# 定数
# ==========================================

BOARD_SIZE = 8

EMPTY = 0
RED = 1
BLUE = 2
GREEN = 3

STONE_COLOR = {
    RED: "red",
    BLUE: "blue",
    GREEN: "limegreen"
}

TURN_NAME = {
    RED: "赤",
    BLUE: "青",
    GREEN: "緑"
}

# ==========================================
# ゲームデータ
# ==========================================

board = document.getElementById("board")
turn_label = document.getElementById("turn")

turn = RED

board_data = [
    [EMPTY for _ in range(BOARD_SIZE)]
    for _ in range(BOARD_SIZE)
]

# 初期配置
board_data[3][3] = RED
board_data[3][4] = BLUE
board_data[4][3] = GREEN
board_data[4][4] = RED
board_data[2][3] = BLUE
board_data[5][4] = GREEN


# ==========================================
# 石を置く
# ==========================================

def place_stone(x, y):

    global turn

    if board_data[y][x] != EMPTY:
        return

    board_data[y][x] = turn

    if turn == RED:
        turn = BLUE

    elif turn == BLUE:
        turn = GREEN

    else:
        turn = RED

    draw_board()


# ==========================================
# 描画
# ==========================================

def draw_board():

    board.replaceChildren()

    for y in range(BOARD_SIZE):

        for x in range(BOARD_SIZE):

            cell = document.createElement("div")
            cell.setAttribute("class", "cell")

            value = board_data[y][x]

            def click(event, x=x, y=y):
                place_stone(x, y)

            cell.addEventListener("click", click)

            if value != EMPTY:

                stone = document.createElement("div")
                stone.setAttribute("class", "stone")

                stone.style.background = STONE_COLOR[value]

                cell.appendChild(stone)

            board.appendChild(cell)

    turn_label.innerText = f"現在の手番：{TURN_NAME[turn]}"


# ==========================================
# メイン
# ==========================================

draw_board()
