# 03day 加载+ORM

#### 加载url链接:

                                 使用url\_for{视图函数名称}

```text
index.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<a href="{{ url_for('login') }}">login</a>
</body>
</html>
```

#### 加载静态文件：

语法： url\_for\('static',filename='xxx/yyy'\) 例子：

```text
 css    <link rel="stylesheet" href="{{ url_for('static',filename='css/index.css') }}">
 javascript   <script src ="{{ url_for('static',filename='js/index.js') }}"></script>
 image     <img src="{{ url_for('static',filename='images/1.jpg') }}" alt="">
 
 static文件夹下是images,css,js三个文件夹
```

ORM

* Object Relationship Mapping（模型关系映射） 
* Flask-sqlalchemy就是ORM框架：pip install flask-sqlalchemy 
* 操作数据库就像是操作对象类（object）,把表抽象成类，一条数据就是一个对象

