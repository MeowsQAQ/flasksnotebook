# 2 Flask基础

### [ToCatalog](../)

## 安装Python2.7：

1. Mac下使用Python3.7.
2. Windows下安装Python.7.
   * 从python官网下载python.7的版本。
   * 双击python.7，然后选择安装路径，一顿下一步就可以了。
   * 设置环境变量，把python的安装路径添加到PATH变量中（安装程序会有选项提示）。
   * 还需要设置一个环境变量，一定要设置，不然后面就不能正常安装flask了。

## Python虚拟环境介绍与安装：

1. 因为python的框架更新迭代太快了，有时候需要在电脑上存在一个框架的多个版本，这时候虚拟环境就可以解决这个问题。
2. 通过以下命令安装虚拟环境：pip install virtualenv
3. 开辟新的虚拟环境：virtualenv \[virtualenv-name\]
4. 激活虚拟环境：
   * \[类linux\]：source \[虚拟环境的目录\]/bin/activate
   * \[windows\]：直接进入到虚拟环境的目录，然后执行activate
   * 退出虚拟环境：deactivate

## pip安装flask：

1. 执行activate脚本，进入指定的虚拟环境。
2. 在该虚拟环境中，执行以下命令安装：pip install flask
3. 验证flask是否安装成功：
   * 进入python命令行。

     > > > import flask print flask.**version**

## 第一个flask程序讲解：

1. 第一次创建项目的时候，要添加flask的虚拟环境。添加虚拟环境的时候，一定要选择到python这个执行文件。

   比如你的flask的虚拟环境的目录在/User/Virtualenv/flask-env/bin/python。

2. flask程序代码的详细解释：

   \`\`\`

   **从flask这个框架中导入Flask这个类**

   from flask import Flask

   **初始化一个Flask对象**

   **Flaks\(\)**

   **需要传递一个参数name**

   **1. 方便flask框架去寻找资源**

   **2. 方便flask插件比如Flask-Sqlalchemy出现错误的时候，好去寻找问题所在的位置**

   app = Flask\(**name**\)

```text
# @app.route是一个装饰器
# @开头，并且在函数的上面，说明是装饰器
# 这个装饰器的作用，是做一个url与视图函数的映射
# 127.0.0.1:5000/   ->  去请求hello_world这个函数，然后将结果返回给浏览器
@app.route('/')
def hello_world():
    return '我是第一个flask程序'


# 如果当前这个文件是作为入口程序运行，那么就执行app.run()
if __name__ == '__main__':
    # app.run()
    # 启动一个应用服务器，来接受用户的请求
    # while True:
    #   listen()
    app.run()
```

```text
#### 设置debug模式：

1. 在app.run\(\)中传入一个关键字参数debug,app.run\(debug=True\)，就设置当前项目为debug模式。
2. debug模式的两大功能：
   * 当程序出现问题的时候，可以在页面中看到错误信息和出错的位置。
   * 只要修改了项目中的`python`文件，程序会自动加载，不需要手动重新启动服务器。

#### 使用配置文件：

1. 新建一个`config.py`文件
2. 在主app文件中导入这个文件，并且配置到`app`中，示例代码如下：

   ```text
    import config
    app.config.from_object(config)
```

1. 还有许多的其他参数，都是放在这个配置文件中，比如`SECRET_KEY`和`SQLALCHEMY`这些配置，都是在这个文件中。

## url传参数：

1. 参数的作用：可以在相同的URL，但是指定不同的参数，来加载不同的数据。
2. 在flask中如何使用参数：

   ```text
    @app.route('/article/<id>')
    def article(id):
        return u'您请求的参数是：%s' % id
   ```

   * 参数需要放在两个尖括号中。
   * 视图函数中需要放和url中的参数同名的参数。

## 反转URL：

1. 什么叫做反转URL：从视图函数到url的转换叫做反转url
2. 反转url的用处：
   * 在页面重定向的时候，会使用url反转。
   * 在模板中，也会使用url反转。

## 页面跳转和重定向：

1. 用处：在用户访问一些需要登录的页面的时候，如果用户没有登录，那么可以让她重定向到登录页面。
2. 代码实现：

   ```text
    from flask import redirect,url
    redirect(url_for('login'))
   ```



