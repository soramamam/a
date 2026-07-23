from pyscript import document

board = document.getElementById("board")

for y in range(8):
    for x in range(8):

        cell = document.createElement("div")
        cell.className = "cell"

        def click(event, x=x, y=y):
            print(f"クリック: ({x}, {y})")

        cell.addEventListener("click", click)

        board.appendChild(cell)
