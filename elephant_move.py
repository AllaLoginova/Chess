def can_bishop_move(start, end):
    # Преобразуем шахматные координаты в числовые
    start_col = ord(start[0]) - ord('a')  # 'a' -> 0, 'b' -> 1, ..., 'h' -> 7
    start_row = int(start[1]) - 1          # '1' -> 0, '2' -> 1, ..., '8' -> 7

    end_col = ord(end[0]) - ord('a')
    end_row = int(end[1]) - 1

    # Проверяем, может ли слон сделать ход
    # Слон может двигаться по диагонали, если разница по столбцам равна разнице по строкам
    return abs(start_col - end_col) == abs(start_row - end_row)

# Чтение входных данных
start_position = input().strip()
end_position = input().strip()

# Проверка и вывод результата
if can_bishop_move(start_position, end_position):
    print("YES")
else:
    print("NO")
