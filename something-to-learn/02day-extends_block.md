# 02day-extends\_block

**继承和block：** 

1.继承语法： ｛% extends 'base.html' %｝ 

2.block 语法:子模板和父模板的block xxx要一致

#### **Code:**

```text
from flask import Flask,render_template
app= Flask (__name__)

class Person(object):
    name=''
    age=0
    def down_page(self):
        pass
class Student(Person):
    def down_page(self):
        print ('xuexi')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```text
index.html:

{% extends 'base.html' %}
{% block title %}
<h1>首页</h1>
{% endblock %}
{% block main %}
<h1>这是首页</h1>
{% endblock %}

```

```text
base.html：

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title%} {% endblock %}</title>
       <style>
        .nav{
            background: #3a3a3a;
            height :65px;}
        ul{
            overflow:hidden;}
        ul li{
            float:left;
            list-style:none;
            padding:0 10px;
            line-height:65px;

        }
        ul li a{
            color:  #fff;}
    </style>
</head>
<body>
<div class="nav">
    <ul><a href="#">首页</a></ul>
    <ul><a href="#">发布问答</a></ul>
</div>

{% block main %} {% endblock %}
</body>
</html>
```

