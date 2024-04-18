from flask import request, jsonify
from config import app, db
from models import Contact


## Decorator
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    # Convert python to json
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


# Run code if in main
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
