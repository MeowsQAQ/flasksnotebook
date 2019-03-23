# 07day cookie+session

**Code：**

```text
app.py：

from flask import Flask,session
import  os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # 24个字符的字符串
print(app.config['SECRET_KEY'])

# 添加数据到session中
# 操作session的时候，跟操作字典是一样的
# secret_key
@app.route('/')
def hello_world():
    session['username'] = 'meows'
    return 'Hello World!'


@app.route('/get/')
def get():
    # session['username']
    # session.get('username')
    print(session.get('username'))
    return session.get('username')


@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'success'

@app.route('/clear/')
def clear():
    print(session.get('username'))
    # 删除session中的所有数据
    session.clear()
    print(session.get('username'))
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
```

