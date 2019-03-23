#encoding:utf-8
from flask import Flask,render_template,request,redirect,url_for,session,g
import config
from models import User, Question, Answer
from exts import db
from decorators import login_required
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user


@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by("create_time").all()
    }
    return render_template('index.html', **context)


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user=User.query.filter(User.telephone == telephone).first()
        if user and user.check_password(password):
            session['user_id']=user.id
            # 如果想在31天都不再次登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '手机号码或者密码错误，请重新输入'


# ?xxx=xxx不需要参数
@app.route('/search/')
def search():
    q = request.args.get('q')
    # title or content
    questions = Question.query.filter(or_(Question.title.contains(q),
                                          Question.content.contains(q))).order_by('create_time')
    return render_template('index.html', questions=questions)


@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method =='GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        # 手机号码验证如果被注册了就不能注册
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '该号码已经注册'
        else:
            # 密码输入一致
            if password!=confirm_password:
                return '两次密码不相等,请核对后在填写'
            else:
                user = User(telephone=telephone, username=username, password=password)
                db.session.add(user)
                db.session.commit()
                # 成功后跳转到登录页面
                return redirect(url_for('login'))


@app.route('/detail/<question_id>/')
def detail(question_id):
    question_content=Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question_content=question_content)


@app.route('/quote/',methods=['POST'])
@login_required
def quote():
    quote_content=request.form.get('quote_content')
    question_id = request.form.get('question_id')
    answer = Answer(content=quote_content)
    answer.author = g.user
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session('user_id')
    session.clear()
    return  redirect(url_for('login'))


@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title,content=content)
        question.author = g.user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.context_processor
def my_context_processor():
    if hasattr(g,'user'):
            return{'user':g.user}
    return {}


if __name__ == '__main__':
    app.run(debug=True)
