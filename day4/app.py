#flask import
from flask import Flask , render_template

#1. app 생성
app = Flask(__name__)

#2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hi.html', name= name)

    
if __name__ == '__main__':
    app.run(debug = True)
