from flask import Flask,session,g
import config
from exts import db,mail

from flask_migrate import Migrate

from blueprints.auth import bp as auth_bp
from blueprints.product import bp as product_bp

from models import UserModel

app=Flask(__name__)
#绑定配置文件
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app,db)

#blueprint:用来模块化
app.register_blueprint(product_bp)
app.register_blueprint(auth_bp)


#flask db init：只需要执行一次
#flask db migrate：将oem模型生成迁移脚本
#flask db upgrade：将迁移脚本映射到数据库中

#before_request/before_first_request/after_request
#hook
@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g,"user",user)
    else:
        setattr(g,"user",None)

@app.context_processor
def my_context_processor():
    return {"user":g.user}


if __name__=='__main__':
    app.debug = True#1.debug模式
    app.run(host='0.0.0.0',port=5000)

