from flask_sqlalchemy import SQLAlchemy

DEFAULT_CUPCAKE_URL= "https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg"

db = SQLAlchemy()


class Cupcake(db.Model):
    """Cupcake"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    flavor = db.Column(db.String(50), nullable=False)

    size = db.Column(db.String(50), nullable=False)

    rating = db.Column(db.Float, nullable=False)

    image_url = db.Column(db.String(50), nullable=False)

    def image_url(self):
        """return image url"""

        return self.image_url or DEFAULT_CUPCAKE_URL
    

def connect_db(app):
    """Connect to the database"""

    db.app = app
    db.init_app(app)