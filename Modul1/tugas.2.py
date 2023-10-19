random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# print(random_list)

float_list = ()
string_list = []
int_data = {}

for item in random_list:
    if isinstance(item, float):
        float_list += (item,)
    elif isinstance(item, str):
        string_list.append(item)
    elif isinstance(item, int):
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 10
        int_data[item] = {"satuan", satuan, "puluhan", puluhan, "ratusan", ratusan}

print(string_list)
print(float_list)
print(int_data)
