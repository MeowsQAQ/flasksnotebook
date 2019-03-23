# 08day before\_request+get post

### [ToCatalog](../)

### Code:

```text
app.py:

  from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/search/')
def search():
    # arguments
    q=request.args.get('q')
    print('请求数据为：%s'% q)
    print(request.args)
    return 'search'

# 默认试图函数，只能采用get请求
# 如果想要采用Post请求，那么要写明
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username=request.form.get('username')
        password=request.form.get('password')
        print(' username:%s\n password:%s'%(username,password))
        return 'post request'
if __name__ == '__main__':
    app.run(debug=True)
```

```text
login.html:
 
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登陆</title>
</head>
<body>
<form action="{{ url_for('login') }}" method="post">
    <table>
        <tbody>
            <tr>
                <td>用户名：</td>
                <td><input type="text" placeholder="请输入用户名" name="username"></td>
            </tr>
            <tr>
                <td>密码：</td>
                <td><input type="text" placeholder="请输入密码" name="password"></td>
            </tr>
            <tr>
                <td></td>
                <td><input type="submit" value="登录"></td>
            </tr>
        </tbody>
    </table>
</form>
</body>
</html>
```

