#flask import
from flask import Flask , render_template, request
import random
#1. app 생성
app = Flask(__name__)


#2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hi.html', name = name)


@app.route('/lunch')
def lunch():
    menus = ['레드코코넛누들', '소불고기', '삼계탕', '싸이버거', '치킨']
    pick = random.choice(menus)
    return render_template('lunch.html', menus = menus, pick = pick)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
# 사용ㅈ가 보낸 데이터를 받아와서 
# 템플릿에 보내기
def pong():
    text = request.args.get('say')
    time = request.args.get('time')
    return render_template('pong.html', text = text, time=time)    

@app.route("/picture")
def find():
    color = request.args.get('color')
    url = "https://www.google.com/search?q={0}+aesthetic&source=lnms".format(color)
    return render_template('picture.html', color = color, url = url )
@app.route('/self2')
def self2():
    name = request.args.get('type')
    return render_template('self2.html', name = name)

@app.route('/naver')
def naver():
    return render_template('naver.html')



@app.route('/number')
def number():
    a = random.randint(1,50)
    number = request.args.get('say')
    if a == number:
        answer = '정답'
        return render_template('number.html', answer = answer)
    else :
        if a > number:
            answer = '큼'
            return render_template('number.html', answer= answer)
        else:
            answer = '작음'
            return render_template('number.html', answer = answer)
       



@app.route('/self')
def self():
    return render_template('self.html')




@app.route('/lotto')
def lotto(): 
    return render_template('lotto.html')


@app.route('/lotto_result')
def lotto2():
    user = request.args.get('name')
    l_num = request.args.get('num')
    random.seed(l_num)   # 난수를 발생시키지만 입력받은 값 이상의 난수를 생성한다? Sorry?
    l_number = random.sample(range(1, 46), 6)
    return render_template('lotto_result.html',name = user, number = l_num, l_number = l_number)

if __name__ == '__main__':
    app.run(debug = True)