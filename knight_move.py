def can_knight_move(start, end):
    # Преобразуем шахматные координаты в числовые
    start_col = ord(start[0]) - ord('a')  # 'a' -> 0, 'b' -> 1, ..., 'h' -> 7
    start_row = int(start[1]) - 1          # '1' -> 0, '2' -> 1, ..., '8' -> 7

    end_col = ord(end[0]) - ord('a')
    end_row = int(end[1]) - 1

    # Вычисляем разницу по координатам
    col_diff = abs(start_col - end_col)
    row_diff = abs(start_row - end_row)

    # Проверяем, может ли конь сделать ход
    return (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)

# Чтение входных данных
start_position = input().strip()
end_position = input().strip()

# Проверка и вывод результата
if can_knight_move(start_position, end_position):
    print("YES")
else:
    print("NO")
