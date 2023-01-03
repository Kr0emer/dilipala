#flask-sqlalchemy
#放置DB对象，解决循环引用，放置第三方插件
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db=SQLAlchemy()
mail=Mail()