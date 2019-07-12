import pprint, requests, random


url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=864"
# 1. 요청
# json -> 
# 파이썬의 dictionary와 list로 변환하여 조작할 수 있다. (pprint를 사용하여)
# 응답(html, xml, json)
response = requests.get(url).json()
pprint.pprint(response)
b = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
for i in range(1,7):
    b.append(response[f'drwtNo{i}'])
s_number = response['bnusNo']


def check() :
    global count1,count2,count3,count4,count5
    my_lotto = random.sample(range(1,46), 6)
    count = 0
    for i in range(0,6):
        for j in range(0, 6):
            if my_lotto[i] == b[j]:
                count += 1

    for i in my_lotto :
        if s_number == i:
            bonus = True
        else:
            bonus = False

    if count == 6:
        
        count1+=1
    elif count == 5 and bonus :
        
        count2+=1
    elif count == 5 and not bonus:
        
        count3+=1
    elif count == 4 :
        
        count4+=1
    elif count == 3 :
        
        count5+=1
  
        

    

for i in range(10000000):
    check()

print("1등 횟수 : {0}".format(count1))
print("2등 횟수 : {0}".format(count2))
print("3등 횟수 : {0}".format(count3))
print("4등 횟수 : {0}".format(count4))
print("5등 횟수 : {0}".format(count5))


#==============================================================================================
# url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
# # 1. 요청
# # json -> 
# # 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
# # 응답 (HTML, XML, JSON)
# response = requests.get(url).json()
# # pprint.pprint(response)
# # print(type(response))

# # 당첨번호 6개 + 보너스 번호
# win_lotto = []
# bonus = response['bnusNo']
# for i in range(1, 7):
#     win_lotto.append(response[f'drwtNo{i}'])

# result = [0, 0, 0, 0, 0]
# for i in range(10000000):
#     # 내가 뽑은 로또 번호
#     my_lotto = random.sample(range(1, 46), 6)

#     # 몇개 맞았는지 확인
#     # matched = 0
#     # for num in my_lotto:
#     #     if num in win_lotto:
#     #         matched += 1
#     matched = len(set(win_lotto) & set(my_lotto))

#     # 몇개 맞았는지를 바탕으로 출력
#     if matched == 6:
#         result[0] += 1
#     elif matched == 5 and bonus in my_lotto:
#         result[1] += 1
#     elif matched == 5:
#         result[2] += 1
#     elif matched == 4:
#         result[3] += 1
#     elif matched == 3:
#         result[4] += 1
#     print(result, end='\r')
# print('끝')
# print(result)
