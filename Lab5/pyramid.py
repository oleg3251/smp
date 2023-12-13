class Pyramid:
    @staticmethod
    def create_pyramid(x, y):
        pyramid = []
        for i in range(y):
            line = ''
            for j in range(x):
                if i == 0:  # for the top of the pyramid
                    line += '+' if j == x // 2 else ' '
                elif i == y - 1:  # drawing the base of the pyramid
                    if j == 0 or j == x - 1:
                        line += '+'  # Place '+' at the beginning and end of the line
                    elif 0 < j < x - 1:
                        line += '-'  # Fill the middle with '-'
                elif j == x // 2 - i or j == x // 2 + i:  # drawing the edges of the pyramid
                    line += '/' if j == x // 2 - i else '\\'
                elif x // 2 - i < j < x // 2 + i:  # drawing the sides of the pyramid
                    line += ' '
                else:
                    line += ' '
            pyramid.append(line)
        return pyramid
