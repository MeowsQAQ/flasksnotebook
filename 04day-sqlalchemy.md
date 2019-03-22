# 04day Sqlalchemy

## **Sqlalchemy连接Mysql**

```text
连接数据库
SQLALCHEMY_DATABASE_URIdialect+driver://username:password@host :port
```

\*\*\*\*

```text
   app.py:


#encoding utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

db.create_all()

@app.route('/')
def index():
    return 'index'

if __name__ =='__main__':
    app.run(debug=True)
```

```text
config.py：


#encoding utf-8

# dialect+driver://username:password@host :port
DIALECT ='mysql'
DRIVER ='mysqldb'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE='db_demo1'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset =utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
```

## **Sqlalchemy模型与表单映射：**

1.Mysql中代码：

```text
 article表:
 create table arlticle(
     id int primary key autoincrement,
     title varchar(100) not null,
     content text not null
 )
```

2.Flask中代码：

```text
class Article(db.Model):
    __tablename__ ='article'                                        //表名，如果没写默认小写class的名字，变量都用 Column函数
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)   //整型 主键 自动增长  
    title = db.Column(db.String(100),nullable=False)                //varvhar char 都是用db.String  非空
    content = db.Column(db.Text,nullable=False)                     //text类型， 非空
 db.create_all()                                                    //创建全部
```

**Code：**

```text
app.py:

#encoding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app =Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

# article表:
# create table arlticle(
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null
# )
class Article(db.Model):
    __tablename__ ='article'
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

db.create_all()
```

```text
config.py:

#encoding utf-8

# dialect+driver://username:password@host :port
DIALECT ='mysql'
DRIVER ='mysqldb'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE='db_demo1'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

