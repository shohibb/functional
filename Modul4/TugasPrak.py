def point(x, y):
    return x, y


def log_inputs(func):
    def wrapper(*args, **kwargs):
        print(f"Calling func with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result

    return wrapper


# @log_inputs
def line_equation_of(p1, M):
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"


from math import sin, cos, radians

translation = lambda tx, ty: lambda p: (p[0] + tx, p[1] + ty)

dilation = lambda sx, sy: lambda p: (p[0] * sx, p[1] * sy)

rotation = lambda edge: lambda p: (
    p[0] * cos(radians(edge)) - p[1] * sin(radians(edge)),
    p[0] * sin(radians(edge)) + p[1] * cos(radians(edge)),
)
x = int(input("enter the x : "))
y = int(input("enter the y : "))
m = float(input("enter the gradient : "))

# Output
print("Persamaan garis yang melalui satu titik :")
print(line_equation_of(point(x, y), m))

# result = log_inputs(line_equation_of(point(x, y), m))
# print(result)


# @log_inputs
def transform(p, tx, ty, edge, sx, sy):
    return dilation(sx, sy)(rotation(edge)(translation(tx, ty)(p)))


tx = float(input("masukan tx :"))
ty = float(input("masukan ty :"))
edge = float(input("masukan edge :"))
sx = float(input("masukan sx :"))
sy = float(input("masukan sy :"))

# Apply transformation to points
p1_transformed = transform(point(x, y), tx, ty, edge, sx, sy)
print(p1_transformed)
# Calculate new line equation based on transformed points
new_line_equation = line_equation_of(p1_transformed, m)

print("Persamaan garis setelah transformasi:")
print(new_line_equation)
