ssafy = {
    'location': ['서울', '대전', '구미', '광주'],
    'language': {
        'python': {
            'python standard library': ['os', 'random', 'webbrowser'],
            'frameworks': {
                'flask': 'micro',
                'django': 'full-functioning'
            },
            'data_science': ['numpy', 'pandas', 'scipy', 'sklearn'],
            'scraping': ['requests', 'bs4'],
        },
        'web' : ['HTML', 'CSS']
    },
    'classes': {
        'dj': {
            'lecturer': 'tak',
            'manager': '노구하',
            'class president': '연용흠',
            'groups': {
                'A': ['송지영', '최성철', '박진희', '박태수', '염동환', '연용흠'],
                'B': ['홍순범', '김준영', '양혜진', '서현택', '최무연', '조선행'],
                'C': ['김태우', '이승열', '장은비', '조병준', '김인성'],
                'D': ['김은정', '이지민', '이경호', '정지수', '염겨레'],
            }
        },
        'gj': {
            'lecturer': 'change',
            'manager': 'gj-pro'
        }
    }
}


"""
난이도* 1. 지역(location)은 몇 개 있나요?
출력예시)
4
"""
print('==== Q1 ====')
print(len(ssafy['location']))

"""
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
False
"""
print('==== Q2 ====')
print('requests' in ssafy['language']['python']['python standard library'])
"""
난이도** 3. dj 반의 반장의 이름을 출력하세요.
출력예시)
연
"""
print('==== Q3 ====')
print(ssafy['classes']['dj']['class president'])
"""
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
"""
print('==== Q4 ====')
for i in ssafy['language'].keys():
    print(i)
"""
난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요.
출력 예시)
change
pro-gj
"""
print('==== Q5 ====')
for i in ssafy['classes']['gj'].values():
    print(i)
"""
난이도***** 6. framework 들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""
print('==== Q6 ====')
for i,j in ssafy['language']['python']['frameworks'].items():
    print("{0}는 {1}이다.".format(i, j))


"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 D 그룹에서 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 김준호
"""
print('==== Q7 ====')
import random
a = random.randint(0,len(ssafy['classes']['dj']['groups']['D'])-1)
print('오늘의 당번은 {0}'.format(ssafy['classes']['dj']['groups']['D'][a]))
print('오늘의 당번은 {0}'.format(random.choice(ssafy['classes']['dj']['groups']['D'])))

dictionary = {'a' : 1, 'b' : 2, 'c' : 3}
print(dictionary.get('d'))
print(dictionary.get('c'))
# dictionary.get(a,b) > (a,b)안에 a가 dictionary안에 존재하는지 확인하고, 존재하면 a를 키로 가지고 있는 값을, 없으면 b을 반환한다.
