from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"

connect_db(app)


@app.route("/")
def home_page():
    """display homepage"""
    return render_template("index.html")


##GET ALL##
@app.route("/api/cupcakes")
def list_all_cupcakes():
    """Return all cupcakes"""

    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]


    return jsonify(cupcakes=cupcakes)


##GET SPECIFIC##
@app.route("/api/cupcakes/<int:cupcake_id>")
def list_single_cupcake(cupcake_id):
    """Return specific cupcake"""

    cupcake = Cupcake.query.get(cupcake_id)

    return jsonify(cupcake=cupcake.to_dict())


##POST NEW CUPCAKE##
@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create cupcake from form data and return it"""

    flavor= request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image_url= request.json["image_url"]

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image_url=image_url or None)
    db.session.add(new_cupcake)
    db.session.commit()

    #return w/status code 201
    return (jsonify(cupcake=new_cupcake.to_dict()), 201)
    # end create_cupcake

##PATCH CUPCAKE##
@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake based on data in the request"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor= request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]
    cupcake.image_url= request.json["image_url"]

    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.to_dict())

##DELETE CUPCAKE##
@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete Cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")