# Second-exts.py/models.py

### 因为需要连接数据库，所以使用`sqlalchemy`连接数据库，为防止循环引用问题，将其放入`exts.py`中

```text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #新建db指代Sqlalchemy
```

### 进行项目前需要对项目所需数据库结构进行分析，即我们需要那些数据

## 首先导入db

```text
from exts import db
```

**用户数据：**

```text
用户信息：
    id:识别判断用户主要途径，int型自增长，主键，自动增长
    telephone:用户注册提交，用户登陆验证。string(11),不可空
    username:用户名，string(30)，不可空
    password:注册是密码确认后存入，登录验证，string(100)。不可空
    
    用户输入用户信息时，要先拦截后将密码加密保证信息安全
```

```text
from werkzeug.security import generate_password_hash,check_password_hash  # 密码加密,验证解密
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # 拦截用户数据，对Password加密
    def __init__(self,*args,**kwargs):
        telephone=kwargs.get('telephone')
        username = kwargs.get('username')
        password = kwargs.get('password')

        self.telephone = telephone
        self.username = username
        # 手机号码，用户名不需要加密直接存入，密码hash加密
        self.password = generate_password_hash(password)
    # 接密hash，验证密码
    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return result
```

#### 问答数据：

```text
问答信息：
    id：对问答进行编号，索引时按编号查找。int，主键，自动增长
    title：问答标题 string(100)，不可空
    content：问答内容 text，不可空
    create_time:问答创建时间,DATETIME,当前默认时间
    author_id:外键连接用户数据， int 外键（user.id）
```

```text
from datetime import datetime
class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db .Column(db.Text,nullable=False)
    # now()获取的是服务器第一次运行的时间，返回结果
    # now是每次创建一个模型的时候的当前时间，返回函数
    create_time = db.Column(db.DATETIME,default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 反转，通过Question.author来操作发布问答的用户数据
    author = db.relationship('User', backref=db.backref('questions'))
```

#### 问答评论数据：

```text
问答信息：
    id:问答编号 int 主键 自动增长
    content:评论内容，Text，不可空
    create_tme:DATATIME，默认为当前时间
    question_id:外键连接问答数据Question，int
    author_id：外键连接用户数据User，id

```

```text
class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text,nullable= False)
    create_time=db.Column(db.DATETIME,default=datetime.now)
    question_id = db.Column(db.Integer,db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    question = db.relationship('Question', backref=db.backref('answers',order_by=id.desc()))
    author = db.relationship('User', backref=db.backref('answers'))
```

#### Mysql数据：

![mysql&#x4E2D;&#x6570;&#x636E;](../.gitbook/assets/image%20%286%29.png)

