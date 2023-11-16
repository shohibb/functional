from math import sin, cos, radians

translation = lambda tx, ty: lambda p: (p[0] + tx, p[1] + ty)

dilation = lambda sx, sy: lambda p: (p[0] * sx, p[1] * sy)

rotation = lambda edge: lambda p: (
    p[0] * cos(radians(edge)) - p[1] * sin(radians(edge)),
    p[0] * sin(radians(edge)) + p[1] * cos(radians(edge)),
)


# def translation(tx, ty):
#     def transform(p):
#         x, y = p
#         return x + tx, y + ty

#     return transform


# def dilation(sx, sy):
#     def transform(p):
#         x, y = p
#         return x * sx, y * sy

#     return transform


# def rotation(edge):
#     def transform(p):
#         x, y = p
#         theta = radians(edge)
#         new_x = x * cos(theta) - y * sin(theta)
#         new_y = x * sin(theta) + y * cos(theta)
#         return new_x, new_y

#     return transform


def main():
    coord = (3, 5)

    # Translasi
    new_translation = translation(2, -1)
    translation_coord = new_translation(coord)
    print("Koordinat setelah translasi:", translation_coord)

    # Dilatasi
    new_dilation = dilation(2, -1)
    dilation_coord = new_dilation(coord)
    print("Koordinat setelah dilatasi:", dilation_coord)

    # Rotasi
    new_rotation = rotation(30)
    rotation_coord = new_rotation(coord)
    print("Koordinat setelah rotasi:", rotation_coord)


if __name__ == "__main__":
    main()
