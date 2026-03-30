class RailFenceCipher:

    def __init__(self):
        pass

    def encrypt(self, message, key):
        rail = ['' for _ in range(key)]
        dir_down = False
        row = 0

        for char in message:
            rail[row] += char

            if row == 0 or row == key - 1:
                dir_down = not dir_down

            row += 1 if dir_down else -1

        return ''.join(rail)

    def decrypt(self, cipher, key):
        rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

        dir_down = None
        row, col = 0, 0

        # Đánh dấu vị trí zig-zag
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1

        # Điền ký tự vào đúng vị trí
        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if rail[i][j] == '*' and index < len(cipher):
                    rail[i][j] = cipher[index]
                    index += 1

        # Đọc lại zig-zag để giải mã
        result = []
        row, col = 0, 0

        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            result.append(rail[row][col])
            col += 1
            row += 1 if dir_down else -1

        return ''.join(result)