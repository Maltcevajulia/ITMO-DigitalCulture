# Пишешь ниже все 9 вероятностей
a = 0.14  # 1
b = 0.12  # 2
c = 0.05  # 3
d = 0.26  # 4
e = 0.01  # 5
f = 0.16  # 6
g = 0.27  # 7
h = 0.03  # 8
k = 0.17  # 9

# Решение
o = (1 - a) * (1 - b) * (1 - c) * (1 - d) * (1 - k)
z = o / (1 - c) - o
print(round(o, 2))
print(round(f, 2))
print(round((1 - h) * (1 - k), 2))
