import random
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
   
    return render_template('hi.html')    

@app.route("/hi")
def hi():
    return "ㅎㅇㅎㅇ"
    
@app.route('/hi/<string:name2>')
def higyo(name2):
    return render_template('hi2.html',name = name2)

@app.route("/cube/<int:number>")
def cal(number):
    return ("{0}".format(number ** 3))    
# 이거 할때 변수 위치 조심하기
@app.route("/lunch/<string:name>")
def lunch(name):
    A = ['한식', '특식A', '특식B']
    return render_template('lunch.html', name=name, food=random.choice(A))  #return f'{name}야, {random.choice(menu)먹어'}
#로또!
#/lotto
#로또 번호 6개 추천해 주는 페이지
# 서버를 포함시킴으로써 동적인 코드를 작성할 수 있게 된다.
@app.route("/lotto")
def lotto():
    s = []
    for i in range(6):
        s.append(random.randint(1, 45))        #- by myself
    # numbers = random.sample(range(1, 46),6)   - by 강사님
    return "오늘의 당첨 번호는 <h1>{0}</h1> 입니다.".format(str(s))
    #python app.py를 실행하면 아래의 코드를 실행한다.
if __name__ == '__main__':
    app.run(debug=True)

#/큐브/?에 숫자가 들어오면 세재곱하는 페이지
