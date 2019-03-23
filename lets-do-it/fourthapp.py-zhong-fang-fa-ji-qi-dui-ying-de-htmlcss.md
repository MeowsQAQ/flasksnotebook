# Fourth-app.py中方法及对应的html/css

### [ToCatalog](../)

## 首先**我们需要导入flask包中的一些类，配置文件config，数据库模型和sqlalchemy操作db以及装饰器中的装饰器，接着将app+db初始化**

```text
from flask import Flask,render_template,request,redirect,url_for,session,g
import config
from models import User, Question, Answer
from exts import db
from decorators import login_required
from sqlalchemy import or_ 

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
```

#### html父模板样式：

需要导入`bootstrap`，并通过`bootstarp`中一些特定类，更改样式,并在代码中设置`block`以供子模版继承后自定义样式

![&#x6A21;&#x677F;&#x6837;&#x5F0F;](../.gitbook/assets/image%20%284%29.png)

#### 主页方法：

```text
@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by("create_time").all()
    }
    return render_template('index.html', **context)
    
# 首页需要展示问答内容，所以需要在数据库中查找问答，并以时间顺序导出传到index.html中
```

继承base.html，在`block main`中for循环遍历`questions`，将其全部展示

#### 注册方法：

![&#x6CE8;&#x518C;&#x65B9;&#x6CD5;](../.gitbook/assets/image.png)

     注册方法中需要用到`get`和`post`两种方法，需要在装饰器中，`get`方法就转入到注册页面。`post`方法时，分别从用户表单中获得`telephone`,`username`,`password`,`confirm_password`这些数据，然后数据库中查看telephone是否已经存在，如果不存在则判断`password`和`confirm_password`是否一致，一致时则创建user并通过`db.session`提交新建到数据库，表示注册完成，再重新跳转到登陆页面

```text
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
```

#### 登陆方法：

![&#x767B;&#x9646;&#x65B9;&#x6CD5;](../.gitbook/assets/image%20%281%29.png)

登陆方法同样需要用到get和post，`post`方法时，在登陆页面表单中读取用户输入的数据，通过用户`telephone`在数据库中查找是否存在用户，若存在用户，则需要通过比对两个`password`是否一致，一致时讲`user.id`传入`session`，返回主页

```text
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
```

#### 登陆后注销方法：

清除session

```text
@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session('user_id')
    session.clear()
    return  redirect(url_for('login'))
```

#### 获取用户方法：

通过上下文处理器钩子函数，将User设为g变量，实现DRY

```text
@app.context_processor
def my_context_processor():
    if hasattr(g,'user'):
            return{'user':g.user}
    return {}
```

#### 发布问答方法：

![&#x53D1;&#x5E03;&#x95EE;&#x7B54;](../.gitbook/assets/image%20%285%29.png)

发布问答时需要判断用户当前是否登陆，如果未登录需要转到`login`页面，这里通过修饰器来实现，新建`decorators.py`文件，写一个判断登陆的装饰器。通过判断后需要使用`POST`方法获取表单信息，然后`session.add()`和`session.commit()`实现数据库更新

```text
from flask import session,redirect,url_for
from functools import wraps


# 登陆限制的装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper

```

```text
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
        return redirect(url_for('index')
```

{% code-tabs %}
{% code-tabs-item title="question.css" %}
```css
.form-container{
    width: 500px;
    margin: 0 auto;
    text-align: right;
}
```
{% endcode-tabs-item %}
{% endcode-tabs %}

#### 问答详情方法：

![&#x95EE;&#x7B54;&#x8BE6;&#x60C5;\(&#x5305;&#x62EC;&#x8BC4;&#x8BBA;\)](../.gitbook/assets/image%20%283%29.png)

需要传入`question_id`参数来确认用户希望查看的是哪一个问答详情，然后通过`question_id`返回数据库中查找问答详情内容，最后返回`detail.html`时需要再把问答详情`question_content`传入

```text
@app.route('/detail/<question_id>/')
def detail(question_id):
    question_content=Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question_content=question_content)
```

需要在detail.html中写入问答评论模块

#### 评论方法：

评论时也需要判断用户是否登陆所以也需要引用装饰器login\_required,则在需要读取用户数据，通过session添加提交，最后转回至问答详情页面将，当前问答Id传入

```text
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
```

.html和.css在问答详情页面

