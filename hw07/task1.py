class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        s = [[str(elem) for elem in row] for row in self.matrix]
        lenghts = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lenghts)
        table = [fmt.format(*row) for row in s]

        return '\n'.join(table)

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                  for i in range(len(self.matrix))]
        return Matrix(result)


# Тесты
m1 = Matrix([[3, 76, 4], [-3, 8, 50], [19, -4, 5]])
m2 = Matrix([[63, 71, 3], [0, 6, 44], [80, 12, -5]])
print(m1, end="\n\n")
print(m2, end="\n\n")
m3 = m1 + m2
print(m3)
