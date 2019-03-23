from exts import db
from datetime import datetime
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
        self.password = generate_password_hash(password)
    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return result


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


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text,nullable= False)
    create_time=db.Column(db.DATETIME,default=datetime.now)
    question_id = db.Column(db.Integer,db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    question = db.relationship('Question', backref=db.backref('answers',order_by=id.desc()))
    author = db.relationship('User', backref=db.backref('answers'))


