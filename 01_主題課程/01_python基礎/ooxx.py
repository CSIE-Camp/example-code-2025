board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
currentPlayer = 'x'

while True:
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = '')
        print()
    print()
    if currentPlayer == 'x':
        print("輪到玩家1")
    else:
        print("輪到玩家2")
    x = int(input("第幾列: "))
    y = int(input("第幾行: "))
    board[x-1][y-1] = currentPlayer
    win = True
    for i in range(3):
        win = win and (board[i][y-1] == currentPlayer)
    if win:
        if currentPlayer == 'x':
            print("玩家1贏了")
        else:
            print("玩家2贏了")
        break
    win = True
    for j in range(3):
        win = win and (board[x-1][j] == currentPlayer)
    if win:
        if currentPlayer == 'x':
            print("玩家1贏了")
        else:
            print("玩家2贏了")
        break
    if (currentPlayer == board[0][0] and board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (currentPlayer == board[2][0] and board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        if currentPlayer == 'x':
            print("玩家1贏了")
        else:
            print("玩家2贏了")
        break
    if currentPlayer == 'x':
        currentPlayer = 'o'
    else:
        currentPlayer = 'x'
    print("=====================")
        