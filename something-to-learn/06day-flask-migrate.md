# 06day Flask-migrate

### [ToCatalog](../)

**Code：**

```text
from flask_script import  Manager
from app import app
from flask_migrate import Migrate,MigrateCommand
from exts import db
from models import Article

#首次迁移时需执行
# init -> migrate ->upgrade
#初始化环境->生成迁移文件->更新迁移
#之后执行需执行
#migrate->upgrade

#模型-> 迁移文件 ->表
manager = Manager(app)


#1.要使用flask_migrate，必须绑定app和db
migrate = Migrate(app,db)

#2.把MigrateCommand命令添加到manager中
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()
```

