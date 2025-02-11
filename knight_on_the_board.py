class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal  # координата по горизонтали (a-h)
        self.vertical = vertical        # координата по вертикали (1-8)
        self.color = color              # цвет коня (black или white)

    def get_char(self):
        return 'N'  # символ, представляющий коня

    def can_move(self, target_horizontal, target_vertical):
        # Преобразуем горизонтальную координату в числовое значение
        h_diff = abs(ord(target_horizontal) - ord(self.horizontal))
        v_diff = abs(target_vertical - self.vertical)

        # Проверяем, может ли конь сделать ход
        return (h_diff == 2 and v_diff == 1) or (h_diff == 1 and v_diff == 2)

    def move_to(self, target_horizontal, target_vertical):
        if self.can_move(target_horizontal, target_vertical):
            self.horizontal = target_horizontal
            self.vertical = target_vertical

    def draw_board(self):
        # Создаем пустое шахматное поле
        board = [['.' for _ in range(8)] for _ in range(8)]

        # Устанавливаем позицию коня
        h_index = ord(self.horizontal) - ord('a')  # Преобразуем 'a'-'h' в 0-7
        v_index = 8 - self.vertical  # Преобразуем 1-8 в 7-0

        board[v_index][h_index] = self.get_char()  # Устанавливаем коня на доске

        # Определяем возможные ходы коня
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for move in knight_moves:
            new_h_index = h_index + move[0]
            new_v_index = v_index + move[1]

            # Проверяем, находится ли новая позиция в пределах доски
            if 0 <= new_h_index < 8 and 0 <= new_v_index < 8:
                board[new_v_index][new_h_index] = '*'  # Отмечаем возможные ходы

        # Печатаем шахматное поле без пробелов
        for row in board:
            print(''.join(row))


# Пример использования
knight = Knight('c', 3, 'white')
knight.draw_board()
