from flask_sqlalchemy import SQLAlchemy

DEFAULT_CUPCAKE_URL= "https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg"

db = SQLAlchemy()


class Cupcake(db.Model):
    """Cupcake"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    flavor = db.Column(db.Text, nullable=False)

    size = db.Column(db.Text, nullable=False)

    rating = db.Column(db.Float, nullable=False)

    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_CUPCAKE_URL)

    def to_dict(self):
        """serialize the cupcake SQLAlchemy obj to dictionary"""
        return {
            "id":self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image_url":self.image_url
        }
    

def connect_db(app):
    """Connect to the database"""

    db.app = app
    db.init_app(app)