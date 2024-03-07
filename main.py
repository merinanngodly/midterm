from flask import Flask
app = Flask(__name__)

@app.route('/add/<num1>/<num2>')
def add(num1,num2):
    return f'<h1>{num1}+{num2}={str(int(num1)+int(num2))}</h1>'

@app.route('/mult/<num1>/<num2>')
def mult(num1,num2):
    return f'<h1>{num1}*{num2}={str(int(num1)*int(num2))}</h2>'

@app.route('/sub/<num1>/<num2>')
def sub(num1,num2):
   return f'<h1>{num1}-{num2}={str(int(num1)-int(num2))}</h2>'
