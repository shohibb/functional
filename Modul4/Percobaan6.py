def point(x, y):
    return x, y


def line_equation_of(p1, M):
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"


# Output
print("Persamaan garis yang melalui satu titik :")
print(line_equation_of(point(1, -3), -5))
