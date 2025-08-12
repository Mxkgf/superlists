配置新网站
======================

## 需要的包:

* nginx
* python 3.6
* virtualenv + pip
* git

以Ubuntu18LTS为例:
sudo apt update && apt upgrade
sudo apt install nginx git python3.6 python3.6-venv

## Nginx虚拟主机
* 参考 nginx.template.conf
* 把SITENAME替换成所需的域名

## Systemd service
* 参考gunicron-systemd.template.service
* 把SITENAME替换成所需的域名

## 文件夹结构
/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
