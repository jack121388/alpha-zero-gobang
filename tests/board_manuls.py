# 测试 win
win_manuals = [
  # O O O O O
  # X X X X -
  # - - - - -
  # - - - - -
  # - - - - -
  [5, [0, 5, 1, 6, 2, 7, 3, 8, 4], 1],  # 横向五
  # O O O O -
  # X X X X X
  # O - - - -
  # - - - - -
  # - - - - -
  [5, [0, 5, 1, 6, 2, 7, 3, 8, 10, 9], -1],  # 白子横向五
  # O O - O O
  # X X X X -
  # O - - - -
  # - - - - -
  # - - - - -
  [5, [0, 5, 1, 6, 10, 7, 3, 8, 4], 0],  # 有一个空位
  # O O O X O
  # X X X X -
  # O - - - -
  # - - - - -
  # - - - - -
  [5, [0, 5, 1, 6, 2, 7, 10, 8, 4], 0],  # 有一个白子
  # O X X X X
  # O - - - -
  # O - - - -
  # O - - - -
  # O - - - -
  [5, [0, 1, 5, 2, 10, 3, 15, 4, 20], 1],  # 纵向五
  # O X X X X
  # O - - - -
  # O - - - -
  # - O - - -
  # O - - - -
  [5, [0, 1, 5, 2, 10, 3, 16, 4, 20], 0],  # 纵向五有一个空位
  # O X X X X
  # O - - - -
  # O - - - -
  # X O - - -
  # O - - - -
  [5, [0, 1, 5, 2, 10, 3, 16, 4, 20, 15], 0],  # 纵向五有一个白子
  # O X X X X
  # - O - - -
  # - - O - -
  # - - - O -
  # - - - - O
  [5, [0, 1, 6, 2, 12, 3, 18, 4, 24], 1],  # 斜线五
  # O X X X X
  # - O - - -
  # - - - O -
  # - - - O -
  # - - - - O
  [5, [0, 1, 6, 2, 12, 3, 19, 4, 24], 0],  # 斜线五有一个空的
  # O X X X X
  # - O - - -
  # - - X O -
  # - - - O -
  # - - - - O
  [5, [0, 1, 6, 2, 12, 3, 19, 4, 24, 18], 0],  # 斜线五有一个白子
  # X X X X O
  # - - - O -
  # - - O - -
  # - O - - -
  # O - - - -
  [5, [4, 0, 8, 1, 12, 2, 16, 3, 20], 1],  # 反斜线五
  # X X X X O
  # - - - O -
  # - - O - -
  # O - - - -
  # O - - - -
  [5, [4, 0, 8, 1, 12, 2, 15, 3, 20], 0],  # 反斜线五 有一个空位
  # X X X - O
  # - - - O -
  # - - O - -
  # - X - - -
  # O - - - -
  [5, [4, 0, 8, 1, 12, 2, 16, 20], 0],  # 反斜线五 有一个空位
]

# valid moves
valid_moves_manuals = [
  # O - - 
  # - - - 
  # - - O 
  [3, [0, 8], [1, 2, 3, 4, 5, 6, 7]],
  # O - - - -
  # - - - - -
  # - - - - -
  # - - - - -
  # - - - - -
  [5, [0], [1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 18]],
  # - - - - -
  # - - - - -
  # - O - - -
  # - - - - -
  # - - - - -
  [5, [11], [0, 1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 17, 18, 20, 21, 22, 23]],

  # - - - - - - - -
  # - - - - - - - -
  # - - - - - - - -
  # - - O - X - - -
  # - - - - - - - -
  # - - - - - - - -
  # - - - - - - - -
  # - - - - - - - -
  [8, [26, 28], [
    8, 9, 10, 11, 12, 13, 14,
    16, 17, 18, 19, 20, 21, 22,
    24, 25, 27, 29, 30,
    32, 33, 34, 35, 36, 37, 38,
    40, 41, 42, 43, 44, 45, 46,
    ],
  ],
]