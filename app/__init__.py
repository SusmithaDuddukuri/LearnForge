import os
from flask import Flask
from .routes import bp
from .repository import init_db

def create_app(test_config=None):
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.update(
        SECRET_KEY=os.environ.get("LEARNFORGE_SECRET_KEY", "dev-only-change-before-deployment"),
        DATABASE=os.environ.get("LEARNFORGE_DATABASE", os.path.join(app.instance_path, "learnforge.sqlite3")),
        TESTING=False,
        MAX_CONTENT_LENGTH=1024 * 1024,
    )
    if test_config:
        app.config.update(test_config)
    os.makedirs(app.instance_path, exist_ok=True)
    with app.app_context():
        init_db()
    app.register_blueprint(bp)
    return app
