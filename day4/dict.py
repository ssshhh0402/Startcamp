# #Dictionary는 Key와 Value로 저장
# #key : String, Integer, float, boolean 가능 / list, dictionary 불가능
# #Value : 모든 값 가능
# dinner = dict(gkstlr = '040404040404044')
# lunch = {"중국집": '123415616'}
# print(dinner)
# bf = {}
# bf['분식']=  '12039ㅕ156-1967987'
# print(bf)
# menu = {'bf':bf, 'lunch':lunch,'dinner':dinner}
# print(menu)
# print(menu['bf'][분식])

ssafy = {'김은정' : '학생', '김인성' : '학생', '연용흠': '반장'}
for i in ssafy:
        print (i)
        print (ssafy[i])


#print(ssafy.items()) >> key와 value를 가지는 튜플들
print(ssafy.items())

for key, value in ssafy.items():
        print(key + value)


#value만 뽑아서 쓰고 싶을때
for value in ssafy.values():
    print(value)


#key만 뽑아서 쓰고 싶을때
for key in ssafy.keys():
    print(key)