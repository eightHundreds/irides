fork from Flask REST Template



# 数据库迁移,命令

```
python manage.py db stamp 版本号 强制修改当前版本
python manage.py db init 创建migrate文件夹 注意这时候数据库是里面的version文件夹是空de
python manage.py db migrate -m "message" 根据模型设置生成迁移文件
python manage.py db history 查看migrate历史
python manage.py db upgrade 版本名 不是"message",写版本号的前缀也行
python manage.py db downgrade
python manage.py db current 查python manager.py看当前版本
```