[![Build Status](https://travis-ci.org/eightHundreds/irides.svg?branch=master)](https://travis-ci.org/eightHundreds/irides)
[![codebeat badge](https://codebeat.co/badges/d536af42-3a52-4dc8-9a13-4465112bed24)](https://codebeat.co/projects/github-com-eighthundreds-irides-master)
[![Coverage Status](https://coveralls.io/repos/github/eightHundreds/irides/badge.svg?branch=master)](https://coveralls.io/github/eightHundreds/irides?branch=master)

fork from [Flask REST Template](https://github.com/alexandre/flask-rest-template)


# 开发注意点

之前设计时是把每个业务模块的model放到相应的业务模块文件夹下,比如`app/users/model.py`
在统一用`app/models.py`来引用每个业务的model类,使用时只需要`from app import model`,`model.User.dosomething`

但现在有人把所有类放到`app/models.py`,但这没关系后面的开发会证明哪种设计更合适,现在只要记住,所有对model的引用都通过`from app import model`方式,这样后面如果要修改也比较方便

# 项目结构说明

```
|- app
	|- users 用户模块
		|- models.py 用户model类型
		|- controllers.py 用户模块业务逻辑
		|- resources.py 对外api
	...
|- migrations 数据库迁移文件
|- doc 文档
|- tests 测试代码
	|- conftest.py 测试固件(Test Fixture)
	|- pytest.ini pytest配置
	|- integration 集成测试
	|- mocks 伪造类
	|- unit 单元测试
|- .travis.yml 持续集成配置
|- .codebeatignore 在线静态代码检测配置
```

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
