# 05day Flask-scripts

### [ToCatalog](../)

Flask-Scripts

```text
from flask_scripts import Manager
manager = Manager()
@manager.command
def  xxx:
    xxxx
    
1.如果在主'manage.py'文件中 那么终端中  'python manage.py command_name'
2.如果把一些命令集中与另一个文件中，那么需要在终端输入命令时，在command_name前面加上一个父命令 ‘python manage.py db command_name’
```

### Code:

```text
app.py:


#encoding:utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```

```text
manage.py:
 

#encoding:utf-8

from flask_script import Manager
from app import app
from db_scripts import DB_manager

manager = Manager(app)

@manager.command
def runserver():
    print('服务器跑起来了')


manager.add_command('db',DB_manager)

if __name__ =='__main__':
    manager.run()
```

```text
db_script.py


from flask_script import Manager

DB_manager = Manager()

@DB_manager.command
def init ():
    print('数据库初始化')

@DB_manager.command
def migrate():
    print('数据库迁移')

```

