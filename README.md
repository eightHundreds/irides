fork from [Flask REST Template](https://github.com/alexandre/flask-rest-template)

# 开发注意点

之前设计时是把每个业务模块的model放到相应的业务模块文件夹下,比如`app/users/model.py`
在统一用`app/models.py`来引用每个业务的model类,使用时只需要`from app import model`,`model.User.dosomething`

但现在有人把所有类放到`app/models.py`,但这没关系后面的开发会证明哪种设计更合适,现在只要记住,所有对model的引用都通过`from app import model`方式,这样后面如果要修改也比较方便


# 数据库迁移,命令
注意在迁移中sqlite不支持删除数据库字段,所以要删除字段的话几乎是要删除所有的版本记录(其实删到这个字段添加的记录就行)
每个migrate都要提交信息
```
python manage.py db stamp 版本号 强制修改当前版本
python manage.py db init 创建migrate文件夹 注意这时候数据库是里面的version文件夹是空de
python manage.py db migrate -m "message" 根据模型设置生成迁移文件
python manage.py db history 查看migrate历史
python manage.py db upgrade 版本名 不是"message",写版本号的前缀也行
python manage.py db downgrade
python manage.py db current 查python manager.py看当前版本
```