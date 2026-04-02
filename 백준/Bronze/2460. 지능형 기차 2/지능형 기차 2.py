cur = 0
m = []

for i in range(10):
    off, on = map(int, input().split())
    cur = cur - off
    cur = cur + on
    m.append(cur)

print(max(m))