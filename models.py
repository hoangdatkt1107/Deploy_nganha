from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy without app to allow importing db before app is created

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)


def init_db(app):
    """Configure the database and create tables if they don't exist."""
    app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///tasks.db')
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)
    with app.app_context():
        db.create_all()