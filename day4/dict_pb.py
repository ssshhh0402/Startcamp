# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.

print('==== Q1 ====')
sum = 0
for i in score.values():
    sum += i
  
print(sum / len(score))
#===============강사님 code==================
# result = 0
# for i in score.values():
#     result += i
# print(result/ len(score))


#=============================================
# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
t_sum = 0
t_num = 0
for c_name in scores:
    sum = 0
    for score in scores[c_name].values(): 
        sum += (score)
        t_num += 1
    t_sum += sum
    print("{0}반의 평균은 {1:0.2f}점 입니다.".format(c_name, sum / len(scores[c_name].values())))
print("전체 평균은 {0:0.2F}점 입니다.".format(t_sum/t_num))

#================================강사님 코드============================================
## 1. 기본풀이 (Total 평균만)
# result = 0
# count = 0

# for score_value in score.values():
#     result = result + score_value
#     count = count + 1
# # 2. sum 함수 활용하기(Total 평균만)
# result2 = sum(score.values())
# count = len(score)
# print(result2/count)

# total_score = 0
# for person_scores in scores.values():
#     for score in person_scores.values():
#         total_score += score
#         count += 1
# print(total_score/count)

#======================================================================================
# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
for name in city:
    for temp in city[name]:
        sum = 0
        sum += temp
    print("{0}의 평균 온도 : {1:0.2f}".format(name, sum / len(city[name])))

#===================================강사님========================================
for name, temp in city.items():
    avg = sum(temp) / len(temp)
    print("{0}의 평균 온도 : {1:0.2f}".format(name, avg))
#==============================================================================


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
max_temp = 0
min_temp = 0

for temp in city.values():
    temp_a = max(temp)
    temp_b = min(temp)
    if temp_a > max_temp:
        max_temp = temp_a
    if temp_b < min_temp:
        min_temp = temp_b

for city_n in city:
    for temp in city[city_n]:
        if temp == max_temp:
            print("가장 더웠던 도시 : {0}".format(city_n))
        elif temp == min_temp:
            print("가장 추웠던 도시 : {0}".format(city_n))

#==============================================강사님================================
# 알고리즘 1: 모든 지역 온도 확인
# min_temp = 0
# max_temp = 0
# min_city = ''
# max_city = ''
# count = 0
# for name, temp in city.items():
# #맨 처음에는 변수들 초기화 하기
#     if count == 0:
#         min_city = name
#         max_city = name
#         min_temp = temp
#         max_temp = temp
#         count += 1
# # 알고리즘 2: 가장 추우면, 해당 도시와 기온 기록
#     if(min(temp)) < min_temp:
#         min_city = name
#         min_temp = min(temp)
# # 알고리즘 3: 가장 더울때도, 기록
#     if(max(temp)) > max_temp:
#         max_city = city
#         max_temp = max(temp)


#===================================================================================


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
for temp in city['서울']:
    if temp == -2:
        answer = True
    else :
        answer = False
if answer:
    print('예')
else :
    print('아니요')

#=================================강사님===============================================
# for temp in city['서울']:
#     Python에서 기본적으로 제공해 주는 내부함수 >> x in 반복가능 객체 >> 반복가능 객체 안에 x가 있는지/없는지(True/False) 반환
#     if 2 in city['서울']:
#         print('예')
#     else:
#         print('아니요')

#======================================================================================