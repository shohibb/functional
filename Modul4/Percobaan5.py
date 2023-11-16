def point(x, y):
    return x, y


def line_equation_of(p1, p2):
    def calculate_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    M = calculate_slope(p1, p2)
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"


# Output
print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(4, -2), point(-1, 3)))
