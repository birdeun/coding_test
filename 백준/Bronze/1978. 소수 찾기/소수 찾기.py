n = int(input())
lst = list(map(int, input().split()))
rst = 0

for num in lst:
    cnt = 0

    for i in range(1, max(lst) + 1):
        if num % i == 0:
            cnt += 1
            if cnt > 2:
                break
    
    if cnt == 2:
        rst += 1
        
print(rst)