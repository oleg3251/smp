class Cube:
    def __init__(self):
        pass

    # draw 2d representation of cube
    @staticmethod
    def create_2d(x, y):
        lst_1 = []
        for i in range(y):
            line = ''
            for j in range(x):
                if i == 0 or i == y - 1:
                    if j == 0 or j == x - 1:
                        line += '+'
                    else:
                        line += '-'
                else:
                    if j == 0 or j == x - 1:
                        line += '|'
                    else:
                        line += ' '
            lst_1 += [line]
        return lst_1

    # Creates starting lines for the 3D cube drawing
    @staticmethod
    def __create_start_line(length, size_z):
        lines = []
        for index in range(length):
            if index < size_z:
                line = ' ' * (size_z - index)
            else:
                line = ''
            lines += [line]
        lines += ['']
        return lines

    # Builds a single line for the 3D cube representation
    @staticmethod
    def __build_line(size_x, index, sym, length):
        line = ''
        for size in range(size_x + 1):
            if index == 0 or index == length:
                line += '+' if size == 0 or size == size_x else '-'
            else:
                line += sym if size == 0 or size == size_x else ' '
        return line

    # draw 3D-cube using ASCII art
    def build_3d(self, size_x, size_y, size_z):
        length_x = size_x + size_z
        length_y = size_y + size_z
        lines = self.__create_start_line(length_y, size_z)
        index = 0
        i = 1
        new_lines = []
        while index <= length_y:
            line = ''
            if size_z > index:
                line = self.__build_line(size_x, index, '/', length_y)
            elif size_z == index:
                line = self.__build_line(size_x, 0, '|', length_y)
            elif size_z < index:
                line = self.__build_line(size_x, index, '|', length_y)

            if size_y > index != 0:
                if length_x - (index + len(line)) >= 0:
                    line += (' ' * (index - 1)) + '|'
                else:
                    line += (' ' * (length_x - len(line))) + '|'
            elif size_y == index:
                if length_x - (index + len(line)) >= 0:
                    line += (' ' * (index - 1)) + '+'
                else:
                    line += (' ' * (length_x - len(line))) + '+'
            elif size_y < index != length_y:
                if len(lines[index]) == 0:
                    line += (' ' * (length_y - index - 1)) + '/'
                else:
                    i += 1
                    line += (' ' * (index - i)) + '/'

            new_lines += [lines[index] + line]

            index += 1

        return new_lines
