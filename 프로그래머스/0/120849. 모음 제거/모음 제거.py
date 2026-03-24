def solution(my_string):
    ans = ''
    for k in my_string:
        if k in ('a','e','i','o','u'):
            continue
        else:
            ans += k
    return ans
