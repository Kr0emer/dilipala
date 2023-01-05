#配置相关
#session的盐
SECRET_KEY = "9ehs7dtehz6xnwhg27"


# MySQL所在的主机名
HOSTNAME = "192.168.137.1"
# MySQL监听的端口号，默认3306
PORT= 3306
#连接MySQL的用户名，读者用自己设置的
USERNAME = "root"
#连接MySQL的密码，读者用自己的
PASSWORD = "199902018854LJHk" 
# MySQL上创建的数据库名称
DATABASE = "demo"

DB_URI="mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


#邮箱配置
MAIL_SERVER = "smtp.163.com"
MAIL_USE_SSL = True 
MAIL_PORT = 465
MAIL_USERNAME = "dilipala2023@163.com"
MAIL_PASSWORD = "TRULOQXJGXHXEIFJ"
MAIL_DEFAULT_SENDER = "dilipala2023@163.com"

