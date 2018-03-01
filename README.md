[![Build Status](https://travis-ci.org/eightHundreds/irides.svg?branch=master)](https://travis-ci.org/eightHundreds/irides)
[![codebeat badge](https://codebeat.co/badges/d536af42-3a52-4dc8-9a13-4465112bed24)](https://codebeat.co/projects/github-com-eighthundreds-irides-master)
[![Coverage Status](https://coveralls.io/repos/github/eightHundreds/irides/badge.svg?branch=master)](https://coveralls.io/github/eightHundreds/irides?branch=master)
[![Heroku Status](https://heroku-badge.herokuapp.com/?app=irides&root=/alive)](https://irides.herokuapp.com)


[swagger doc](http://petstore.swagger.io/?url=https://irides.herokuapp.com/api/swagger.json)

# irides

图片网

# 开始

**安装**

```
pip install -r requirement.txt
npm install 或者 yarn
```

**预处理**

```
python manage.py seed #初始化数据库
npm run build
```

**运行**

```
python manage.py runserver
```
访问[http://127.0.0.1:5000](http://127.0.0.1:5000)

如果只要看前端
```
npm run dev
```

# 测试

- 测试前安装requirements_test.txt
- conftest.py中是testfixture,尽可能在测试方法(注意是测试方法而不是普通的方法)用这些对象
- 如果测试失败,并显示 outside of application context. 只需要在测试方法传入app参数(app是个testfixture)

# 开发

参考[wiki](https://github.com/eightHundreds/irides/wiki/开发)

# 感谢

- [Flask REST Template](https://github.com/alexandre/flask-rest-template)
- [vue-admin-flask-example](https://github.com/bay1/vue-admin-flask-example)
