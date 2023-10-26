data = [
    3.1,
    "apple",
    2.7,
    5,
    5.5,
    "banana",
    100,
    277,
    737,
    "hello",
    "python",
    "world",
    "AI",
]

float_values = list(filter(lambda x: isinstance(x, float), data))
int_values = list(filter(lambda x: isinstance(x, int), data))
str_values = list(filter(lambda x: isinstance(x, str), data))


def map_to_units(value):
    ratusan = value // 100
    puluhan = (value // 10) % 10
    satuan = value % 10
    return {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}


int_mapped = list(map(map_to_units, int_values))

print("Data Float:")
print(tuple(float_values))
print("Data Int:")
for entry in int_mapped:
    print(entry)
print("Data String:")
print(str_values)
