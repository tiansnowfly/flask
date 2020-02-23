# flask框架学习

**1.flask框架文件结构**
flask框架文件结构中主要分为两种，一种是分区式，一种是功能式。

```python
# 分区式
yourapp/
    __init__.py
    admin/
        __init__.py
        views.py
        static/
        templates/
    home/
        __init__.py
        views.py
        static/
        templates/
    control_panel/
        __init__.py
        views.py
        static/
        templates/
    models.py
```

```python
# 功能式
yourapp/
    __init__.py
    static/
    templates/
        home/
        control_panel/
        admin/
    views/
        __init__.py
        home.py
        control_panel.py
        admin.py
    models.py
```

但平时我们单一模块的应用直接使用如下比较简单的结构：

```python
# 单一模块
yourapp/
	tempaltes/
	static/
	__init__.py
	app.py
	config.py
	requirements.txt
```

| templates        | 放置应用的jinja2模板                                         |
| ---------------- | ------------------------------------------------------------ |
| static           | 包括了公共CSS， Javascript, images和其他你想通过你的应用展示出去的静态文件.默认情况下人们可以从yourapp.com/static/获取这些文件。 |
| \__init\__.py    | 初始化应用并且将其他的组件组合在一起                         |
| app.py           | 这里定义了路由。它也许需要作为一个包（yourapp/app/），由一些包含了紧密相联的路由的模块组成。 |
| config.py        | 配置变量参数                                                 |
| requirements.txt | 列出python依赖包                                             |

**2.创建虚拟环境,激活并运行app**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200220134346506.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z4dDUyMA==,size_16,color_FFFFFF,t_70)
**3.创建flask应用**
最基本的架构：

```python
# 基本架构
blog\
	venv\
	app\
    		static\
    		templates\
		__init__.py
		routes.py
        	config.py
        	requirements.txt
```

进入blog目录下面创建一个app目录，app目录下面创建一个__init__.py文件,代码:

```python
from flask import Flask
//创建一个应用程序对象
app=Flask(__name__)
```

__name__是预定义python变量,表示当前调用flask的模块的名字。当需要加载资源的时候，flask就是用这个位置作为起点来计算出绝对路径。
