#### 模板
**采用jinja2模板引擎**

+ {{ var }}:中包含变量

+ {%  %}: 写入控制语句

#### 表单
+ 在python文件当中定义字段类对象
+ 然后再html文件中将字段渲染为html元素即可
+ 提交表单的时候使用form.validate_on_submit()实例方法进行校验工作
+ 当用户再浏览器中点击提交按钮的时候，浏览器会向服务器发送post请求，form.validate_on_submit()就会获取数据，运行各个字段然后进行验证，全部同过就会返回True。表示提交的表单有效。
+ 表单有效提交之后就会可以使用后redirect进行路由重定向跳转到指定网页。