import os
#window - cp949
#mac/ .... = utf-8
# with open('ssafy_with.txt','r') as f:
    #readlines()는 라인을 각각 리스트의 원소로 가지고 온다.
    #readlines()는 list 형태로 반환한다.
    # lines = f.readlines()
    # print(lines)
    # print(type(lines))
    # for line in lines:
    #     print(line.strip())

# read()는 str의 형태로 반환한다.
# with open ('ssafy_with.txt', 'r') as f:
#     txt = f.read()
#     print(txt)
#     print(type(txt))

with open ('number.txt.txt', 'r') as f:
    read = f.readlines()
    b = list(reversed(read))
    print(b)