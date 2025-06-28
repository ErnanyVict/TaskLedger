from flask import Flask
from PackageResource import package_bp
from TaskResource import task_bp
from UserResource import user_bp



app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/taskledger')
app.register_blueprint(task_bp, url_prefix='/taskledger')
app.register_blueprint(package_bp, url_prefix='/taskledger')

if __name__ == '__main__':
    app.run(debug=True)