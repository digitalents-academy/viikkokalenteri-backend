from flask import Flask, jsonify, request, make_response

try:
    from .interface import database as db
except ImportError as e:
    print(str(e))

app = Flask(__name__)

# Adding a calendar marking
@app.route("/v1/calendar/", methods=['POST'])
def add_entry() -> None:

    connection = db.ConnectionString()
    calendar = db.Calendar(connection.connection)

    req = request.get_json()

    location = "The Void"
    info = "No description"

    try:
        subject = req['subject']
        owner = req['owner']
        date = req['date']
        time = req['time']
        if 'location' in req:
            location = req['location']
        if 'info' in req:
            info = req['info']

    except KeyError as e:
        return e, 400

    # Send the request json to the database.

    return make_response(req), 200

@app.route("/v1/calendar/<string:subject>", methods=['DELETE'])
def delete_entry(subject: str) -> None:
    return jsonify({
    'test': subject
    })

@app.route("/v1/calendar/<string:subject>", methods=['PUT'])
def edit_entry(subject: str) -> None:
    return jsonify({
    'test': subject
    })

@app.route("/v1/calendar/<int:entry_id>", methods=['GET'])
def get_entry(entry_id) -> None:
    return jsonify({
    'test': entry_id
    })

@app.route("/v1/calendar/working", methods=['POST'])
def set_working_time() -> None:
    pass

@app.route("/v1/calendar/working", methods=['PUT'])
def update_working_time() -> None:
    pass

if __name__ == "__main__":
    app.run(debug=True)