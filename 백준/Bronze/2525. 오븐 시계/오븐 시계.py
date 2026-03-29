a,b = map(int, input().split())
c = int(input())

m = b + c

if m // 60 > 0:
    a = a + (m // 60)
    m = m % 60
    
    if a >= 24:
        a = a % 24

print(a, m)