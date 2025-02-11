def can_pawn_move(start, end, color):
    # Преобразуем шахматные координаты в числовые
    start_col = ord(start[0]) - ord('a')  # 'a' -> 0, 'b' -> 1, ..., 'h' -> 7
    start_row = int(start[1]) - 1          # '1' -> 0, '2' -> 1, ..., '8' -> 7

    end_col = ord(end[0]) - ord('a')
    end_row = int(end[1]) - 1

    # Определяем направление движения в зависимости от цвета пешки
    if color == 'white':
        direction = 1  # Пешка движется вверх
        start_initial_row = 1  # Начальная позиция для белых
    else:
        direction = -1  # Пешка движется вниз
        start_initial_row = 6  # Начальная позиция для черных

    # Проверяем обычный ход вперед
    if end_col == start_col and end_row == start_row + direction:
        return True

    # Проверяем возможность двойного хода с начальной позиции
    if (start_row == start_initial_row and 
        end_col == start_col and 
        end_row == start_row + 2 * direction):
        return True

    # Проверяем возможность захвата по диагонали
    if abs(end_col - start_col) == 1 and end_row == start_row + direction:
        return True

    return False

# Чтение входных данных
start_position = input().strip()
end_position = input().strip()
color = input().strip().lower()  # 'white' или 'black'

# Проверка и вывод результата
if can_pawn_move(start_position, end_position, color):
    print("YES")
else:
    print("NO")
