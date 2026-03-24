def solution(my_string, letter):
    rst = []
    for i in my_string:
        if i != letter:
            rst.append(i)
        else:
            continue
    return ''.join(rst)