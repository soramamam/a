from pyscript import document

board = document.getElementById("board")

# ----------------------------
# 盤面データ
# ----------------------------

board_data = [[0 for _ in range(8)] for _ in range(8)]

# 初期配置（3色）
board_data[3][3] = 1
board_data[3][4] = 2
board_data[4][3] = 3
board_data[4][4] = 1
board_data[2][3] = 2
board_data[5][4] = 3

# ----------------------------
# 描画
# ----------------------------

def draw_board():

    board.innerHTML = ""

    colors = {
        1: "red",
        2: "blue",
        3: "limegreen"
    }

    for y in range(8):

        for x in range(8):

            cell = document.createElement("div")
            cell.setAttribute("class", "cell")

            value = board_data[y][x]

            if value != 0:

                stone = document.createElement("div")
                stone.setAttribute("class", "stone")
                stone.style.background = colors[value]

                cell.appendChild(stone)

            board.appendChild(cell)


draw_board()
