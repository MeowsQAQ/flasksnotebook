# 01day beginning

代码如下:

```text
from flask import Flask
app = Flask(name)
@app.route('/') 
def index(): 
    return 'Hello World!'
@app.route('/') 
    def user(username): 
    return "Hello {}".format(username)
if name == 'main': 
    app.run() 
```

然后手动的去更改一下网址，如下。看上去还不错。

简单说一下路由:

app = Flask\(**name**\)

```text
@app.route('/') 
def index(): 
    return 'Hello World!' 
```

简单说一下这个部分代码，app = Flask\(**name**\)，用来创建一个Flask应用，一般Flask类构造函数只有一个必须指定的参数，即程序主模块或包的名字，在大多数程序中，Python的**name\_**变量就是所需要的值。 @app.route\('/'\) 这个东西叫路由，程序实例需要知道对每个URL\(网址\)请求运用那些代码，所以保存了一个URL到Python函数的映射关系。处理URL和函数之间的关系的程序称为路由。而下面所修饰的index\(\)函数被叫做视图函数，他来展示你的web页面的样子。

## Templates:

**Code：**

```text
  app.py：


#encoding:utf-8
#从flask这个框架中导入Flask这个类
from flask import Flask,url_for,redirect,render_template
import config

#初始化一个Flask对象
#Flask（）
#需要传递一个参数__name__
#1.方便flask框架去寻找资源
#2.方便flask插件比如Flask-Sqlalchemy出现错误的时候，好去寻找问题所在位置
app = Flask(__name__)
app.config.from_object(config)
#app.route是一个装饰器
# @开头，并且在函数的上面，说明是装饰器
#这个装饰器的作用是做一个url与试图函数的映射
#127.0.01：5000/  ->去请求hello_world这个函数，然后将结果返回给浏览器



from flask import request


@app.route('/')
def index():
    user = {
        'username':'meows',
        'age':18
    }

    return render_template('index.html',user=user)

# @app.route('/<is_login>/')
# def index(is_login):
#     if is_login =='1':
#         user = {
#             'username':'meows',
#             'age':18
#         }
#         return render_template('index.html',user=user)
#     else:
#         return render_template('index.html')


# class Person(object):
#        name='meows',
#         age=18
#
#    meows =Person()
#     context ={
#         'username':'meows',
#         'gender' :'male',
#         'age':18,
#         'person':meows,
#         'websites':{
#             'baidu':'www.baidu.com',
#             'google': 'www.google.com'
#         }
#
#     }
#     return render_template('index.html',**context)

    # login_url =url_for('login')
    # return redirect(login_url)
    # return '这是首页'


    # print (url_for('my_list'))
    #print (url_for('user',name='qaq'))
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s</p>'%user_agent

# @app.route('/login/')
# def login():
#     return '这是登陆页面'
# @app.route('/user/<name>')
#
# @app.route('/question/<is_login>/')
# def question(is_login):
#     if is_login =='1':
#         return '这是发布问答页面'
#     else:
#         return redirect(url_for('login'))
#
# def user(name):
#     return'<h1>hello,%s!</h1>'%name
#
# @app.route('/list/')
# def my_list():
#     return 'list'

#如果当前这个文件是作为入口程序运行，那就执行app.run()
if __name__ == '__main__':
    #app.run()
    #启动一个应用服务器，来接受用户的请求
    #while True;
    #监听内容listen()
    #debug模式
    app.run(Debug=True)
  
```

```text
  index.html:
  
  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{#    这是HTML文件中出现的文字#}
{#    <p>username：{{ username }}</p>#}
{#    <p>gender：{{ gender }}</p>#}
{#    <p>age：{{ age }}</p>#}
{##}
{#    <hr>#}
{#    <p>name:{{ person.name  }}</p>#}
{#    <p>age:{{ person.age }}</p>#}
{##}
{#    <hr>#}
{#    <p>baidu:{{ websites.baidu }}</p>#}
{#    <p>google:{{ websites.google }}</p>#}
{#   if语句#}
{#    {% if user %}#}
{#        <a href="#">{{ user.username }}</a>#}
{#        <a href="#">注销</a>#}
{#    {% else% %}#}
{#        <a href = "#">登陆</a>#}
{#        <a href = "#">注册</a>#}
{##}
{#    {% endif %}#}


{#    For语句#}
    {% for k,v in user.items() %}
        <p> {{ k }}:{{ v }}</p>
    {% endfor %}

</body>
</html>
```

