from src import app
from flask import Flask,make_response,request,render_template,abort,Response,jsonify
import requests

@app.route('/')
def index():
  return 'hello johnson'

@app.route('/setcookie')
def setcookie():
    r=make_response('hurray..!setting cookie!')
    r.set_cookie('name','johnson')
    r.set_cookie('age','20')
    return r

@app.route('/getcookie')
def getcookie():
    name=request.cookies.get('name')
    age=request.cookies.get('age')
    return 'hello '+name+"! "+"you are "+age+" years old!"

@app.route('/robots.txt')
def robots():
    abort(401)

@app.route('/html')
def gethtml():
    return render_template('hello.html')

@app.route('/input',methods=['GET','POST'])
def input():
    if request.method=='POST':
        name=request.form['uname']
        return 'hello '+name
    return render_template('form.html')

@app.route('/authors',methods=['GET'])
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    users = {d['id']:{'name':d['name'],'count':0} for d in data}
    for post in posts:
        users[post['userId']]['count']+=1
    return render_template('authors.html',users=users)
