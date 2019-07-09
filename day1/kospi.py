import requests 
from bs4 import BeautifulSoup
#변수로 선언한 url을 사용하여 요청(request)를 보낸다
# pip install requests : 요청을 보내주는 패키지
# pip install bs4 : 문서를 차직 편하게 바꿔주는 패키지(파싱)
url = 'http://finance.naver.com/sise/'
response = requests.get(url).text
#BeautifulSoup의 역활: request를 파이썬이 찾기 편한 형식으로 문서를 변경한다.
soup = BeautifulSoup(response, 'html.parser')
#KOSPI 찾기
kospi = soup.select_one('#KOSPI_now').text
print(kospi)
