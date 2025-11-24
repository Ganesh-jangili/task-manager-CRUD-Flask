from flask import Flask
from config import mongo

from routes.users import users_bp
from routes.tasks import tasks_bp

app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskmyDatabase"
mongo.init_app(app)

app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(tasks_bp, url_prefix="/tasks")

@app.route("/")
def home():
    return {"message": "Flask Task API running"}

if __name__ == "__main__":
    app.run(debug=True)
    