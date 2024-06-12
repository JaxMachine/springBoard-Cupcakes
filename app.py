from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'

connect_db(app)


def serialize_cupcake(cupcake):
    """serialize the cupcake SQLAlchemy obj to dictionary"""

    return {
        "id":cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.raiting,
        "image_url":cupcake.image_url
    }

##GET ALL##
@app.route("/api/cupcakes")
def list_all_cupcakes():
    """Return all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)


##GET SPECIFIC##
@app.route("/api/cupcakes/<cupcake_id>")
def list_single_cupcake(cupcake_id):
    """Return specific cupcake"""

    cupcake = Cupcake.query.get(cupcake_id)
    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialized)


##POST NEW CUPCAKE##
@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create cupcake from form data and return it"""

    flavor= request.json["flavor"]
    size = request.json["size"]
    image_url= request.json["image_url"]

    new_cupcake = Cupcake(flavor=flavor, size=size, image_url=image_url)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)

    #return w/status code 201
    return (jsonify(cupcake=serialized), 201)
    # end create_cupcake