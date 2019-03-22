# 09day decorator

## Code:

```text
def my_log(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        print('hello world')
        func(*args,**kwargs)
    return wrapper


@my_log   # run = my_log(run) = wrapper   run() = wrapper()
def run():
    print('run')
print('1')
# run.__name__代表的是run1这个函数的名称
print(run.__name__)
print('1')
@my_log
def add(a,b):
    print('hello world')
    c = a+b
    print('结果是:%s'% c)


add(1,2)
run()
```

