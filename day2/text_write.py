#Option 1
#파일 열기
# open('파일명', 옵션)
#옵션 >> w = 덮어쓰기, a = append의 약자(이어쓰기),
f = open('saffy.txt', 'a')
#글을 작성한다.
for i in range(10):
    #\n : 개행문자 >> 줄 띄우는 문자( == 엔터)

    f.write('안녕하세요.{} \n '.format(i))

#파일 닫기(필수!)
f.close()


#Option 2. 컨택스트 매니저(context manager) with 구문
with open('ssafy_with.txt', 'w') as f:
    for i in range(5):
        f.writelines(['은정\n','인성\n'])
