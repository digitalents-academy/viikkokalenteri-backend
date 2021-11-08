from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/v1/calendar/", methods=['POST'])
def add_entry() -> None:
    return jsonify({
    'test': 'test'
    })

@app.route("/v1/calendar/<int:entry_id>", methods=['DELETE'])
def delete_entry(entry_id) -> None:
    return jsonify({
    'test': entry_id
    })

@app.route("/v1/calendar/<int:entry_id>", methods=['PUT'])
def edit_entry(entry_id) -> None:
    return jsonify({
    'test': entry_id
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