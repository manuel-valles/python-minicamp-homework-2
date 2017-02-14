from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'January 09 1983'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello {}!'.format(name)
#This is another way:
# def greeting(name):
#     return 'Hello ' + name + '!'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return str(num1+num2)
#This is another way:
# @app.route('/add/<num1>/<num2>')
# def add(num1,num2):
#     return str(int(num1)+int(num2))

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1,num2):
    return str(num1*num2)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1,num2):
    return str(num1-num2)

@app.route('/favoritefoods/<mylist>')
def favoritefoods(mylist):
    return jsonify(mylist)
