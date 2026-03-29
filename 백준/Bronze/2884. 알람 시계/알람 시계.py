h,m = map(int, input().split())

if m < 45:
    m = m + 60
    h = h - 1
    if h < 0:
        h = h + 24

print(h, m - 45)