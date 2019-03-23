# Third-manage.py/config.py

将数据库连接的基本信息加入到config.py中，sqlalchemy连接数据可格式为：

```text
# dialect+driver://username:password@host :port
```

```text
config.py:
#使用pymysql连接mysql
DIALECT ='mysql'
DRIVER ='pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE='myqa'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS=False
```

创建`manage.py`通过`Flask_scripts`进行命令行操作，实现数据库初始化新建更新功能。需要导入`db`以及`models.py`中的数据模型，命令行操作也需要导入app主程序

```text
#命令

from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from app import app
from exts import db
from models import User, Question, Answer

manager = Manager(app)

#使用Migrate绑定app和db
migrate = Migrate(app,db)

#添加迁移脚本的命令道Manager中
manager.add_command('db',MigrateCommand)


if __name__ =="__main__":
    manager.run()
```

在Terminal中输入

```text
python manage.py db init  # 只有首次运行才进行初始化
python manage.py db migrate # 生成迁移文件 在migrations文件中
python manage.py db upgrade #进行数据库新建更新
```

