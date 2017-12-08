from flask import Flask,make_response,request,render_template,abort,Response
from urllib import urlopen
import json
app=Flask(__name__)

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


@app.route('/authors')
def authors():

    def inner():
         count=0
         url1 = urlopen('https://jsonplaceholder.typicode.com/users').read()
         authors = json.loads(url1)
         url2 = urlopen('https://jsonplaceholder.typicode.com/posts').read()
         posts = json.loads(url2)
         yield '<h3>Author  ||  Count</h3>'
         for x in range(len(authors)):
            id1=authors[x]['id']
            name=authors[x]['name']
            count=0
            for y in range(len(posts)):
               id2=posts[y]['userId']
               if id1==id2:
                 count+=1

            yield'\t%s\t'%name
            yield '->%s<br/>\n' %count
    return Response(inner(), mimetype='text/html')


if __name__=='__main__':
  app.run()
