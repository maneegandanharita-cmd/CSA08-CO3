import copy
rows, cols = 3, 4
bad = [[0] * cols] * rows
bad[0][1] = 7
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7
print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])
stops = {(13.0827, 80.2707): "Chennai Central",
         (13.0418, 80.2341): "T. Nagar"}
print(stops[(13.0418, 80.2341)])
original = [[1, 2], [3, 4]]
alias = original
shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0][0] = 99
print("Alias:", alias)
print("Shallow:", shallow)
print("Deep:", deep)
try:
    stops[[13.0418, 80.2341]] = "Invalid key"
except TypeError as e:
    print("List key error:", e)
