# Django Admin
应用实践

## 环境依赖

* Python 3.6+
* Django 2.0+
* MariaDB 5.5

## 安装

1. 安装Python 3
2. 安装Python第三方包
```
misc/install.sh
```
3. 安装数据库
```
misc/db/install_mysql.sh
```


## 启动

1. 修改Django配置文件，数据库相关的配置 
2. 初始化数据库
```
reinit_db.sh
```
3. 初始化静态文件
```
reinit_static.sh
```
4. 启动Django应用
```
startup.sh
```
